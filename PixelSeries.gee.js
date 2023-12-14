var geometry = ee.Geometry.Point([103.6839, -65.9559])
Map.centerObject(geometry, 10)

var s2 = ee.ImageCollection("COPERNICUS/S1_GRD");

var filtered = s2.filter(ee.Filter.date('2021-01-01', '2022-01-01')).filter(ee.Filter.bounds(geometry))

var SnowChart = ui.Chart.image.seriesByRegion({
  imageCollection: filtered,
  reducer: ee.Reducer.mean(),
  regions: filtered,
  seriesProperty: 'HH'
}).setOptions({
    title: 'HH',
    vAxis: {title: 'HH'},
    hAxis: {title: 'Date', format: 'MM-yy', gridlines: {count: 12}},
})
print(SnowChart)