import math
import numpy

#: Earth radius in km.
EARTH_RADIUS = 6371.0


def _point_at(origin, horizontal_distance, vertical_increment, azimuth):
    """
    Perform a forward geodetic transformation: find a point lying at a given
    distance from a reference one on a great circle arc defined by azimuth, and
    also move the point by a given vertical increment.
    :param origin:
        Dictionary containing the coordinates of a reference point;
        keys include lon, lat in decimal degrees and depth in km.
    :param horizontal_distance:
        Horizontal distance to the target point in km.
    :param vertical_increment:
        Vertical increment from the origin to the target point in km.
    :param azimuth:
        An azimuth of a great circle arc of interest measured in a reference
        point in decimal degrees.
    :returns:
        Dictionary containing the longitude "lon", latitude "lat", and
        depth "dep" of the target point.
    """
    lon, lat = numpy.radians(origin["lon"]), numpy.radians(origin["lat"])
    tc = numpy.radians(360 - azimuth)
    sin_dists = numpy.sin(horizontal_distance / EARTH_RADIUS)
    cos_dists = numpy.cos(horizontal_distance / EARTH_RADIUS)
    sin_lat = numpy.sin(lat)
    cos_lat = numpy.cos(lat)

    sin_lats = sin_lat * cos_dists + cos_lat * sin_dists * numpy.cos(tc)
    sin_lats = sin_lats.clip(-1., 1.)
    lats = numpy.degrees(numpy.arcsin(sin_lats))

    dlon = numpy.arctan2(numpy.sin(tc) * sin_dists * cos_lat,
                         cos_dists - sin_lat * sin_lats)
    lons = numpy.mod(lon - dlon + numpy.pi, 2 * numpy.pi) - numpy.pi
    lons = numpy.degrees(lons)

    deps = origin["depth"] + vertical_increment

    target = {"lon": lons, "lat": lats, "depth": deps}

    return target


def _get_rupture_length_subsurface(mag, rake, method):
    """
    The values are a function of both magnitude and rake.
    Setting the rake to ``None`` causes their "All" rupture-types
    to be applied.
    """
    
    if method == 'length':
        assert rake is None or -180 <= rake <= 180
        if rake is None:
            # their "All" case
            return 10.0 ** (-2.44 + 0.59 * mag)
        elif (-45 <= rake <= 45) or (rake >= 135) or (rake <= -135):
            # strike slip
            return 10.0 ** (-2.57 + 0.62 * mag)
        elif rake > 0:
            # thrust/reverse
            return 10.0 ** (-2.42 + 0.58 * mag)
        else:
            # normal
            return 10.0 ** (-1.88 + 0.50 * mag)
    
    elif method == 'area_ar1':
        assert rake is None or -180 <= rake <= 180
        if rake is None:
            # their "All" case
            return numpy.sqrt(10.0 ** (-3.49 + 0.91 * mag))
    
        elif (-45 <= rake <= 45) or (rake >= 135) or (rake <= -135):
            # strike slip
            return numpy.sqrt(10.0 ** (-3.42 + 0.90 * mag))
        elif rake > 0:
            # thrust/reverse
            return numpy.sqrt(10.0 ** (-3.99 + 0.98 * mag))
        else:
            # normal
            return numpy.sqrt(10.0 ** (-2.87 + 0.82 * mag))
    
    elif method == 'area_ar2':
        assert rake is None or -180 <= rake <= 180
        if rake is None:
            # their "All" case
            return numpy.sqrt(2*(10.0 ** (-3.49 + 0.91 * mag)))
    
        elif (-45 <= rake <= 45) or (rake >= 135) or (rake <= -135):
            # strike slip
            return numpy.sqrt(2*(10.0 ** (-3.42 + 0.90 * mag)))
        elif rake > 0:
            # thrust/reverse
            return numpy.sqrt(2*(10.0 ** (-3.99 + 0.98 * mag)))
        else:
            # normal
            return numpy.sqrt(2*(10.0 ** (-2.87 + 0.82 * mag)))
        

def _get_rupture_width(mag, rake):
    """
    The values are a function of both magnitude and rake.
    Setting the rake to ``None`` causes their "All" rupture-types
    to be applied.
    """
    assert rake is None or -180 <= rake <= 180
    if rake is None:
        # their "All" case
        return 10.0 ** (-1.01 + 0.32 * mag)
    elif (-45 <= rake <= 45) or (rake >= 135) or (rake <= -135):
        # strike slip
        return 10.0 ** (-0.76 + 0.27 * mag)
    elif rake > 0:
        # thrust/reverse
        return ((10.0 ** (-3.99 + 0.98 * mag)) / 2.0) ** 0.5
    else:
        # normal
        return 10.0 ** (-1.14 + 0.35 * mag)


def get_rupture_surface(mag, hypocenter, strike, dip, rake, method):
    """
    Create and return rupture surface object with given properties.
    :param mag:
        Magnitude value, used to calculate rupture dimensions.
    :param hypocenter:
        Dictionary containing the coordinates of the rupture's hypocenter;
        keys include lon, lat in decimal degrees and depth in km.
    :param strike:
        Point representing rupture plane's strike angle, in decimal degrees.
    :param dip:
        Point representing rupture plane's dip angle, in decimal degrees.
    :param rake:
        Point representing rupture plane's rake angle, in decimal degrees.
    :returns:
        Dictionary of the four vertices of a plane; keys are
        "topLeft", "topRight", "bottomLeft", "bottomRight".
    """
    rdip = math.radians(dip)
    aspect_ratio = 1

    # precalculated azimuth values for horizontal-only and vertical-only
    # moves from one point to another on the plane defined by strike
    # and dip:
    azimuth_right = strike
    azimuth_down = (azimuth_right + 90) % 360
    azimuth_left = (azimuth_down + 90) % 360
    azimuth_up = (azimuth_left + 90) % 360

    rup_length = _get_rupture_length_subsurface(mag, rake, method)
    
    if method == 'area_ar1':
        rup_width = rup_length
    elif method == 'area_ar2':
        rup_width = rup_length/2
    else:
        rup_width = _get_rupture_width(mag, rake)
        
    # calculate the height of the rupture being projected
    # on the vertical plane:
    rup_proj_height = rup_width * math.sin(rdip)
    # and its width being projected on the horizontal one:
    rup_proj_width = rup_width * math.cos(rdip)

    # half height of the vertical component of rupture width
    # is the vertical distance between the rupture geometrical
    # center and it's upper and lower borders:
    hheight = rup_proj_height / 2.
    # calculate how much shallower the upper border of the rupture
    # is than the upper seismogenic depth:
    vshift = hheight - hypocenter["depth"]
    # if it is shallower (vshift > 0) than we need to move the rupture
    # by that value vertically.

    rupture_center = hypocenter

    if vshift > 0:
        # we need to move the rupture center to make the rupture plane
        # lie below the surface
        hshift = abs(vshift / math.tan(rdip))
        rupture_center = _point_at(
            hypocenter,
            horizontal_distance=hshift, vertical_increment=vshift,
            azimuth=azimuth_down)

    # From the rupture center we can now compute the coordinates of the
    # four corners by moving along the diagonals of the plane. This seems
    # to be better then moving along the perimeter, because in this case
    # errors are accumulated that induce distorsions in the shape with
    # consequent raise of exceptions when creating PlanarSurface objects
    # theta is the angle between the diagonal of the surface projection
    # and the line passing through the rupture center and parallel to the
    # top and bottom edges. Theta is zero for vertical ruptures (because
    # rup_proj_width is zero)
    theta = math.degrees(
        math.atan((rup_proj_width / 2.) / (rup_length / 2.))
    )
    hor_dist = math.sqrt(
        (rup_length / 2.) ** 2 + (rup_proj_width / 2.) ** 2
    )

    left_top = _point_at(
        rupture_center,
        horizontal_distance=hor_dist,
        vertical_increment=-rup_proj_height / 2.,
        azimuth=(strike + 180 + theta) % 360
    )
    right_top = _point_at(
        rupture_center,
        horizontal_distance=hor_dist,
        vertical_increment=-rup_proj_height / 2.,
        azimuth=(strike - theta) % 360
    )
    left_bottom = _point_at(
        rupture_center,
        horizontal_distance=hor_dist,
        vertical_increment=rup_proj_height / 2.,
        azimuth=(strike + 180 - theta) % 360
    )
    right_bottom = _point_at(
        rupture_center,
        horizontal_distance=hor_dist,
        vertical_increment=rup_proj_height / 2.,
        azimuth=(strike + theta) % 360
    )
    rupture_plane = {"topLeft": left_top,
                     "topRight": right_top,
                     "bottomLeft": left_bottom,
                     "bottomRight": right_bottom}
    return rupture_plane
