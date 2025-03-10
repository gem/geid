# RUPTURE INFORMATION
    
## Rupture details

| atribute             | description          |
|:---------------------|:---------------------|
| Fault mechanism       | Normal               |
| Tectonic region type | Active Shallow Crust |

### Preferred nodal plane solution

| source   |   longitude |   latitude |   depth |   strike |     dip |   rake |   mag |
|:---------|------------:|-----------:|--------:|---------:|--------:|-------:|------:|
| EFEHR    |     13.1    |    42.88   |     7.5 |  168.922 | 55.1786 |    -80 |  6.09 |
| GCMT     |     13.11   |    42.88   |    12   |  152.001 | 34.9999 |    -94 |  6.1  |
| INGV     |     13.1192 |    42.9211 |     5.7 |  159.004 | 46.9999 |    -93 |  6.09 |
| USGS     |     13.0666 |    42.9564 |    10   |  157.891 | 50.09   |    -89 |  6.1  |

### Rupture figure

![](earthquake_ruptures.png)

## References

- `USGS.json`: USGS rupture. https://earthquake.usgs.gov/product/shakemap/us1000725y/atlas/1594393869242/download/rupture.json. Last accessed December 2022.
- `GCMT.PDF`: Global CMT Catalog. https://www.globalcmt.org/cgi-bin/globalcmt-cgi-bin/CMT5/form?
- `EFEHR` - Rupture obtained from project https://gitlab.seismo.ethz.ch/efehr/esrm20_scenario_tests/-/tree/main
- `INGV` - Rupture obtained from https://itaca.mi.ingv.it/ItacaNet_32/#/event/EMSC-20161026_0000095. Last accessed February 2022.

## Notes

- The rupture geometry in `xml` defined by USGS generates a strike in OpenQuake of 337.932 (despite indicating in the `xml` a value of 155). Therefore the order of the right and left coordinates was modified, generating now in OQ a strike value of 157.891.