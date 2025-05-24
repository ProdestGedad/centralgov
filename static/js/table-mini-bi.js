!function () {
  let mainContainer = document.getElementById('table-charts');

  for (let _mcsk of Array.from(mainContainer.style))
    mainContainer.style[_mcsk] = null;
  for (let _mcci of mainContainer.classList)
    mainContainer.classList.remove(_mcci);
  for (let _mcc of mainContainer.childNodes)
    mainContainer.removeChild(_mcc);
  for (let _mca of Array.from(mainContainer.attributes))
    if (_mca.name !== 'id')
      mainContainer.removeAttribute(_mca.name);
  
  let chartsContainer = document.createElement('div');
  mainContainer.appendChild(chartsContainer);
  chartsContainer.classList.add('row');
  let chartsHeading = document.createElement('h3');
  chartsHeading.appendChild(document.createTextNode('Indicadores'))
  chartsHeading.classList.add('col-12');
  chartsContainer.appendChild(chartsHeading);

  let filtersContainer = document.createElement('div');
  mainContainer.appendChild(filtersContainer);
  filtersContainer.classList.add('row');
  let filtersHeading = document.createElement('h3');
  filtersHeading.appendChild(document.createTextNode('Filtros'))
  filtersHeading.classList.add('col-12');
  filtersContainer.appendChild(filtersHeading);

  let microdataContainer = document.createElement('div');
  mainContainer.appendChild(microdataContainer);
  microdataContainer.classList.add('row');
  let microdataHeading = document.createElement('h3');
  microdataHeading.appendChild(document.createTextNode('Microdados'))
  microdataHeading.classList.add('col-12');
  microdataContainer.appendChild(microdataHeading);

  let limparFiltrosBtn = document.createElement('div');
  filtersHeading.appendChild(document.createTextNode(' '));
  filtersHeading.appendChild(limparFiltrosBtn);
  limparFiltrosBtn.classList.add('btn');
  limparFiltrosBtn.classList.add('btn-sm');
  limparFiltrosBtn.classList.add('btn-outline-secondary');
  {
    let _fa = document.createElement('i');
    _fa.classList.add('fa');
    _fa.classList.add('fa-times');
    limparFiltrosBtn.appendChild(_fa);
  }
  limparFiltrosBtn.appendChild(document.createTextNode(' Limpar Alterações'));


  if (typeof chartsActiveFilters === 'undefined') {
    window.chartsActiveFilters = {};
  }
  if (typeof chartsNumbers === 'undefined') {
    window.chartsNumbers = {};
  }
  if (typeof chartsFilters === 'undefined') {
    window.chartsFilters = {};
  }
  if (typeof tableRecords === 'undefined') {
    window.tableRecords = [];
  }
  if (typeof chartsDefinitions === 'undefined') {
    window.chartsDefinitions = [];
  }

  for (let chartFilterName of Object.keys(chartsFilters)) {
    if (!(chartFilterName in chartsActiveFilters)) {
      chartsActiveFilters[chartFilterName] = new Set();
    }
  }

  let summarize = function (mode, series) {
    switch (mode) {
      case 'count':
        return Array.from(series).length;
      case 'countdist':
        return Array.from(new Set(series)).length;
      case 'max':
        return Array.from(series).reduce((pr, a) => (a > (pr ?? a)) ? (pr ?? a) : (a), undefined);
      case 'min':
        return Array.from(series).reduce((pr, a) => (a < (pr ?? a)) ? (pr ?? a) : (a), undefined);
      case 'avg':
        return Array.from(series).length > 0 ? (Array.from(series).reduce((ps, a) => ps + a, 0) / Array.from(series).length) : 0;
      case 'sum':
      default:
        return Array.from(series).reduce((ps, a) => ps + a, 0);
    }
  }
  
  let graficosInstancias = {};
  let graficosCharts = {};

  let update_charts = () => {
    const filteredData = tableRecords.filter(record => {
      for (let [column, forbiddenSet] of Object.entries(chartsActiveFilters)) {
        if (forbiddenSet.has(record[column])) {
          return false;
        }
      }
      return true;
    });
    const chartsFiltersFiltered = Object.fromEntries(Object.entries(chartsFilters).map(([k, v])=> [k, v.filter(o=> !chartsActiveFilters[k].has(o))]));
    for (let chartDefinition of chartsDefinitions) {
      if (graficosCharts[chartDefinition.titulo] !== undefined) {
        graficosCharts[chartDefinition.titulo].destroy();
      }
      let chartInstance = graficosInstancias[chartDefinition.titulo];
      for (let _cc of Array.from(chartInstance.childNodes))
        chartInstance.removeChild(_cc);
      let chartTitle = document.createElement('h5');
      chartTitle.appendChild(document.createTextNode(chartDefinition.titulo));
      chartInstance.appendChild(chartTitle);
      let chartChart= document.createElement('div');
      chartInstance.appendChild(chartChart);
      let options = {
        chart: {
          type: chartDefinition.tipo,
          height: 400,
          ...chartDefinition.grafextras,
          animations: {
            enabled: false
          }
        },
        series: (chartDefinition.grupo === '' ? [''] : chartsFiltersFiltered[chartDefinition.grupo]).map(grupo => ({
          'name': grupo,
          'data': (chartsFiltersFiltered[chartDefinition.eixo] ?? ['']).map(eixo => 
            summarize(chartDefinition.modo,
              filteredData.filter(
                row => (
                  (chartDefinition.grupo === '' ? grupo === '' : row[chartDefinition.grupo] === grupo) &&
                  row[chartDefinition.eixo] === eixo && 
                  (!chartDefinition.prefiltro || !!row[chartDefinition.prefiltro])
                )
              ).map(r => r[chartDefinition.unidade]),
            )
          )
        })
        ),
        xaxis: {
          categories: chartsFiltersFiltered[chartDefinition.eixo] ?? ['']
        },
        ...chartDefinition.rootextras,
      };
      for (let i = 0; i < options.xaxis.categories.length; i++) {
        if (options.series.reduce((k, x) => k && (x.data[i] === 0), true)) {
          options.xaxis.categories.splice(i, 1);
          options.series.forEach(x => x.data.splice(i, 1));
          i--;
        }
      }
      let chart = new ApexCharts(chartChart, options);
      chart.render();
      graficosCharts[chartDefinition.titulo] = chart;
    }
    if (typeof table !== 'undefined') {
      table.clear();
      table.rows.add(filteredData.map(row=>tableColumns.map(col=>row[col]))).draw();
    }
  };

  for (let chartDefinition of chartsDefinitions) {
    if (!(chartDefinition.titulo in graficosInstancias)) {
      let largura = chartDefinition.largura12 ?? 12;
      let graf = document.createElement('div');
      graf.classList.add(`col-${largura}`);
      chartsContainer.appendChild(graf);
      graficosInstancias[chartDefinition.titulo] = graf;
    }
  }

  for (let [chartFilterName, chartFilterValues] of Object.entries(chartsFilters)) {
    let _cfn = chartFilterName;
    let filterContainer = document.createElement('div');
    filtersContainer.appendChild(filterContainer);
    filterContainer.classList.add('col-2');
    let filterTitle = document.createElement('h4');
    filterContainer.appendChild(filterTitle);
    filterTitle.appendChild(document.createTextNode(chartFilterName));
    filterTitle.appendChild(document.createTextNode(' '));
    let invertSelectionButton = document.createElement('span');
    {
      let _fa = document.createElement('i');
      _fa.classList.add('fa');
      _fa.classList.add('fa-shuffle');
      invertSelectionButton.appendChild(_fa);
    }
    invertSelectionButton.appendChild(document.createTextNode(' '));
    invertSelectionButton.appendChild(document.createTextNode('Inverter'));
    filterTitle.appendChild(invertSelectionButton);
    invertSelectionButton.classList.add('btn');
    invertSelectionButton.classList.add('btn-sm');
    invertSelectionButton.classList.add('btn-outline-secondary');
    invertSelectionButton.onclick = ()=>{
      let _s = new Set(Array.from(chartsActiveFilters[_cfn]));
      let _its = Array.from(filterContainer.querySelectorAll('input:not(:checked)'))
      let _ifs = Array.from(filterContainer.querySelectorAll('input:checked'))
      for (let _it of _its)
        _it.checked = true;
      for (let _if of _ifs)
        _if.checked = false;
      let _n = new Set(
        Array.from(chartsFilters[_cfn]).filter(x=> !_s.has(x))
      );
      chartsActiveFilters[_cfn] = _n;
      console.log([[..._s], [..._n]]);
      update_charts();
    }
    for (let chartFilterValue of chartFilterValues) {
      let filterItemLabel = document.createElement('label');
      let filterItemCheck = document.createElement('input');
      filterItemCheck.setAttribute('type', 'checkbox');
      filterItemLabel.classList.add('d-block');
      filterItemLabel.appendChild(filterItemCheck);
      filterItemLabel.appendChild(document.createTextNode(' '));
      filterItemLabel.appendChild(document.createTextNode(chartFilterValue));
      filterContainer.appendChild(filterItemLabel);
      filterItemCheck.checked = true;
      let _cfv = chartFilterValue;
      filterItemCheck.onchange = () => {
        if (chartsActiveFilters[_cfn].has(_cfv)) {
          chartsActiveFilters[_cfn].delete(_cfv);
          filterItemCheck.checked = true;
        } else {
          chartsActiveFilters[_cfn].add(_cfv);
          filterItemCheck.checked = false;
        }
        update_charts();
      }
    }
  }
  limparFiltrosBtn.onclick = () => {
    for (let _i of Array.from(filtersContainer.querySelectorAll('input:not(:checked)'))) {
      _i.checked = true;
    }
    for (let chartFilterName of Object.keys(chartsFilters)) {
      chartsActiveFilters[chartFilterName] = new Set();
    }
    update_charts();
  }
  update_charts();
} ();