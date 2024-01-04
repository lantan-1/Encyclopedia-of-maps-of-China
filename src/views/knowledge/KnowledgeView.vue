<script setup lang="ts">
import { reactive } from 'vue'
import Echarts from '@/components/ReEcharts.vue'
// import { populationBarService } from '@/api/map'

let option1 = reactive({
  animation: true,
  animationThreshold: 2000,
  animationDuration: 1000,
  animationEasing: 'cubicOut',
  animationDelay: 0,
  animationDurationUpdate: 300,
  animationEasingUpdate: 'cubicOut',
  animationDelayUpdate: 0,
  aria: {
    enabled: false
  },
  color: [
    '#5470c6',
    '#91cc75',
    '#fac858',
    '#ee6666',
    '#73c0de',
    '#3ba272',
    '#fc8452',
    '#9a60b4',
    '#ea7ccc'
  ],
  series: [
    {
      type: 'bar',
      name: '2013\u5e74',
      legendHoverLink: true,
      data: [
        '2125',
        '1410',
        '7288',
        '3535',
        '2455',
        '4365',
        '2668',
        '3666',
        '2448',
        '8192',
        '5784',
        '5988',
        '3885',
        '4476',
        '9746',
        '9573',
        '5798',
        '6600',
        '11270',
        '4731',
        '920',
        '3011',
        '8109',
        '3632',
        '4641',
        '317',
        '3804',
        '2537',
        '571',
        '666',
        '2285'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2014\u5e74',
      legendHoverLink: true,
      data: [
        '2171',
        '1429',
        '7323',
        '3528',
        '2449',
        '4358',
        '2642',
        '3608',
        '2467',
        '8281',
        '5890',
        '5997',
        '3945',
        '4480',
        '9808',
        '9645',
        '5816',
        '6611',
        '11489',
        '4770',
        '936',
        '3043',
        '8139',
        '3677',
        '4653',
        '325',
        '3827',
        '2531',
        '576',
        '678',
        '2325'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2015\u5e74',
      legendHoverLink: true,
      data: [
        '2188',
        '1439',
        '7345',
        '3519',
        '2440',
        '4338',
        '2613',
        '3529',
        '2458',
        '8315',
        '5985',
        '6011',
        '3984',
        '4485',
        '9866',
        '9701',
        '5850',
        '6615',
        '11678',
        '4811',
        '945',
        '3070',
        '8196',
        '3708',
        '4663',
        '330',
        '3846',
        '2523',
        '577',
        '684',
        '2385'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2016\u5e74',
      legendHoverLink: true,
      data: [
        '2195',
        '1443',
        '7375',
        '3514',
        '2436',
        '4327',
        '2567',
        '3463',
        '2467',
        '8381',
        '6072',
        '6033',
        '4016',
        '4496',
        '9973',
        '9778',
        '5885',
        '6625',
        '11908',
        '4857',
        '957',
        '3110',
        '8251',
        '3758',
        '4677',
        '340',
        '3874',
        '2520',
        '582',
        '695',
        '2428'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2017\u5e74',
      legendHoverLink: true,
      data: [
        '2194',
        '1410',
        '7409',
        '3510',
        '2433',
        '4312',
        '2526',
        '3399',
        '2466',
        '8423',
        '6170',
        '6057',
        '4065',
        '4511',
        '10033',
        '9829',
        '5904',
        '6633',
        '12141',
        '4907',
        '972',
        '3144',
        '8289',
        '3803',
        '4693',
        '349',
        '3904',
        '2522',
        '586',
        '705',
        '2480'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2018\u5e74',
      legendHoverLink: true,
      data: [
        '2192',
        '1383',
        '7426',
        '3502',
        '2422',
        '4291',
        '2484',
        '3327',
        '2475',
        '8446',
        '6273',
        '6076',
        '4104',
        '4513',
        '10077',
        '9864',
        '5917',
        '6635',
        '12348',
        '4947',
        '982',
        '3163',
        '8321',
        '3822',
        '4703',
        '354',
        '3931',
        '2515',
        '587',
        '710',
        '2520'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2019\u5e74',
      legendHoverLink: true,
      data: [
        '2190',
        '1385',
        '7447',
        '3497',
        '2415',
        '4277',
        '2448',
        '3255',
        '2481',
        '8469',
        '6375',
        '6092',
        '4137',
        '4516',
        '10106',
        '9901',
        '5927',
        '6640',
        '12489',
        '4982',
        '995',
        '3188',
        '8351',
        '3848',
        '4714',
        '361',
        '3944',
        '2509',
        '590',
        '717',
        '2559'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2020\u5e74',
      legendHoverLink: true,
      data: [
        '2189',
        '1387',
        '7464',
        '3490',
        '2403',
        '4255',
        '2399',
        '3171',
        '2488',
        '8477',
        '6468',
        '6105',
        '4161',
        '4519',
        '10165',
        '9941',
        '5745',
        '6645',
        '12624',
        '5019',
        '1012',
        '3209',
        '8371',
        '3858',
        '4722',
        '366',
        '3955',
        '2501',
        '593',
        '721',
        '2590'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2021\u5e74',
      legendHoverLink: true,
      data: [
        '2189',
        '1373',
        '7448',
        '3480',
        '2400',
        '4229',
        '2375',
        '3125',
        '2489',
        '8505',
        '6540',
        '6113',
        '4187',
        '4517',
        '10170',
        '9883',
        '5830',
        '6622',
        '12684',
        '5037',
        '1020',
        '3212',
        '8372',
        '3852',
        '4690',
        '366',
        '3954',
        '2490',
        '594',
        '725',
        '2589'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    },
    {
      type: 'bar',
      name: '2022\u5e74',
      legendHoverLink: true,
      data: [
        '2184',
        '1363',
        '7420',
        '3481',
        '2401',
        '4197',
        '2348',
        '3099',
        '2475',
        '8515',
        '6577',
        '6127',
        '4188',
        '4528',
        '10163',
        '9872',
        '5844',
        '6604',
        '12657',
        '5047',
        '1027',
        '3213',
        '8374',
        '3856',
        '4693',
        '364',
        '3956',
        '2492',
        '595',
        '728',
        '2587'
      ],
      realtimeSort: false,
      showBackground: false,
      stackStrategy: 'samesign',
      cursor: 'pointer',
      barMinHeight: 0,
      barCategoryGap: '20%',
      barGap: '30%',
      large: false,
      largeThreshold: 400,
      seriesLayoutBy: 'column',
      datasetIndex: 0,
      clip: true,
      zlevel: 0,
      z: 2,
      label: {
        show: false,
        margin: 8
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    }
  ],
  legend: [
    {
      data: [
        '2013\u5e74',
        '2014\u5e74',
        '2015\u5e74',
        '2016\u5e74',
        '2017\u5e74',
        '2018\u5e74',
        '2019\u5e74',
        '2020\u5e74',
        '2021\u5e74',
        '2022\u5e74'
      ],
      selected: {},
      show: true,
      padding: 5,
      itemGap: 10,
      itemWidth: 25,
      itemHeight: 14,
      backgroundColor: 'transparent',
      borderColor: '#ccc',
      borderWidth: 1,
      borderRadius: 0,
      pageButtonItemGap: 5,
      pageButtonPosition: 'end',
      pageFormatter: '{current}/{total}',
      pageIconColor: '#2f4554',
      pageIconInactiveColor: '#aaa',
      pageIconSize: 15,
      animationDurationUpdate: 800,
      selector: false,
      selectorPosition: 'auto',
      selectorItemGap: 7,
      selectorButtonGap: 10
    }
  ],
  tooltip: {
    show: true,
    trigger: 'item',
    triggerOn: 'mousemove|click',
    axisPointer: {
      type: 'line'
    },
    showContent: true,
    alwaysShowContent: false,
    showDelay: 0,
    hideDelay: 100,
    enterable: false,
    confine: false,
    appendToBody: false,
    transitionDuration: 0.4,
    textStyle: {
      fontSize: 14
    },
    borderWidth: 0,
    padding: 5,
    order: 'seriesAsc'
  },
  xAxis: [
    {
      name: '\u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40',
      show: true,
      scale: false,
      nameLocation: 'end',
      nameGap: 15,
      gridIndex: 0,
      axisLabel: {
        show: true,
        rotate: -35,
        margin: 8
      },
      inverse: false,
      offset: 0,
      splitNumber: 5,
      minInterval: 0,
      splitLine: {
        show: true,
        lineStyle: {
          show: true,
          width: 1,
          opacity: 1,
          curveness: 0,
          type: 'solid'
        }
      },
      data: [
        '\u5317\u4eac\u5e02',
        '\u5929\u6d25\u5e02',
        '\u6cb3\u5317\u7701',
        '\u5c71\u897f\u7701',
        '\u5185\u8499\u53e4\u81ea\u6cbb\u533a',
        '\u8fbd\u5b81\u7701',
        '\u5409\u6797\u7701',
        '\u9ed1\u9f99\u6c5f\u7701',
        '\u4e0a\u6d77\u5e02',
        '\u6c5f\u82cf\u7701',
        '\u6d59\u6c5f\u7701',
        '\u5b89\u5fbd\u7701',
        '\u798f\u5efa\u7701',
        '\u6c5f\u897f\u7701',
        '\u5c71\u4e1c\u7701',
        '\u6cb3\u5357\u7701',
        '\u6e56\u5317\u7701',
        '\u6e56\u5357\u7701',
        '\u5e7f\u4e1c\u7701',
        '\u5e7f\u897f\u58ee\u65cf\u81ea\u6cbb\u533a',
        '\u6d77\u5357\u7701',
        '\u91cd\u5e86\u5e02',
        '\u56db\u5ddd\u7701',
        '\u8d35\u5dde\u7701',
        '\u4e91\u5357\u7701',
        '\u897f\u85cf\u81ea\u6cbb\u533a',
        '\u9655\u897f\u7701',
        '\u7518\u8083\u7701',
        '\u9752\u6d77\u7701',
        '\u5b81\u590f\u56de\u65cf\u81ea\u6cbb\u533a',
        '\u65b0\u7586\u7ef4\u543e\u5c14\u81ea\u6cbb\u533a'
      ]
    }
  ],
  yAxis: [
    {
      name: '\u5355\u4f4d\uff1a\u4e07\u4eba',
      show: true,
      scale: false,
      nameLocation: 'end',
      nameGap: 15,
      gridIndex: 0,
      inverse: false,
      offset: 0,
      splitNumber: 5,
      minInterval: 0,
      splitLine: {
        show: true,
        lineStyle: {
          show: true,
          width: 1,
          opacity: 1,
          curveness: 0,
          type: 'solid'
        }
      }
    }
  ],
  title: [
    {
      show: true,
      text: '\u8fd1\u5341\u5e74\u5404\u7701\u603b\u4eba\u53e3\u67f1\u72b6\u56fe',
      target: 'blank',
      subtarget: 'blank',
      padding: 5,
      itemGap: 10,
      textAlign: 'auto',
      textVerticalAlign: 'auto',
      triggerEvent: false
    }
  ]
})
let option2 = reactive({
  animation: true,
  animationThreshold: 2000,
  animationDuration: 1000,
  animationEasing: 'cubicOut',
  animationDelay: 0,
  animationDurationUpdate: 300,
  animationEasingUpdate: 'cubicOut',
  animationDelayUpdate: 0,
  aria: {
    enabled: false
  },
  color: [
    '#5470c6',
    '#91cc75',
    '#fac858',
    '#ee6666',
    '#73c0de',
    '#3ba272',
    '#fc8452',
    '#9a60b4',
    '#ea7ccc'
  ],
  series: [
    {
      type: 'funnel',
      name: '\u77ff\u4ea7\u50a8\u91cf',
      data: [
        {
          name: '\u77f3\u6cb9\u50a8\u91cf(\u4e07\u5428)',
          value: '350120.3'
        },
        {
          name: '\u5929\u7136\u6c14\u50a8\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '54365.5'
        },
        {
          name: '\u7164\u70ad\u50a8\u91cf(\u4ebf\u5428)',
          value: '2492.3'
        },
        {
          name: '\u9530\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '31033.6'
        },
        {
          name: '\u539f\u751f\u949b\u94c1\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '23065.1'
        },
        {
          name: '\u94dc\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '2621'
        },
        {
          name: '\u950c\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '4439.1'
        },
        {
          name: '\u94dd\u571f\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '100955.3'
        },
        {
          name: '\u91d1\u77ff\u50a8\u91cf(\u5428)',
          value: '2021.5'
        },
        {
          name: '\u94f6\u77ff\u50a8\u91cf(\u5428)',
          value: '40611.1'
        },
        {
          name: '\u83f1\u9541\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '100772.5'
        },
        {
          name: '\u666e\u901a\u8424\u77f3\u50a8\u91cf(\u4e07\u5428)',
          value: '4229.2'
        },
        {
          name: '\u786b\u94c1\u77ff\u50a8\u91cf(\u4e07\u5428)',
          value: '127809'
        },
        {
          name: '\u94be\u76d0\u50a8\u91cf(\u4e07\u5428)',
          value: '56212'
        },
        {
          name: '\u91cd\u6676\u77f3\u50a8\u91cf(\u4e07\u5428)',
          value: '3626.2'
        },
        {
          name: '\u73bb\u7483\u7845\u8d28\u539f\u6599\u50a8\u91cf(\u4e07\u5428)',
          value: '196374.7'
        },
        {
          name: '\u77f3\u58a8\u50a8\u91cf(\u4e07\u5428)',
          value: '7321.5'
        },
        {
          name: '\u6ed1\u77f3\u50a8\u91cf(\u4e07\u5428)',
          value: '8204.6'
        },
        {
          name: '\u9ad8\u5cad\u571f\u50a8\u91cf(\u4e07\u5428)',
          value: '69285.1'
        }
      ],
      sort: 'ascending',
      gap: 0,
      label: {
        show: true,
        margin: 8
      }
    }
  ],
  legend: [
    {
      data: [
        '\u94be\u76d0\u50a8\u91cf(\u4e07\u5428)',
        '\u94f6\u77ff\u50a8\u91cf(\u5428)',
        '\u7164\u70ad\u50a8\u91cf(\u4ebf\u5428)',
        '\u77f3\u6cb9\u50a8\u91cf(\u4e07\u5428)',
        '\u91cd\u6676\u77f3\u50a8\u91cf(\u4e07\u5428)',
        '\u9ad8\u5cad\u571f\u50a8\u91cf(\u4e07\u5428)',
        '\u83f1\u9541\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u9530\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u73bb\u7483\u7845\u8d28\u539f\u6599\u50a8\u91cf(\u4e07\u5428)',
        '\u94dc\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u77f3\u58a8\u50a8\u91cf(\u4e07\u5428)',
        '\u5929\u7136\u6c14\u50a8\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u94dd\u571f\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u786b\u94c1\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u950c\u77ff\u50a8\u91cf(\u4e07\u5428)',
        '\u666e\u901a\u8424\u77f3\u50a8\u91cf(\u4e07\u5428)',
        '\u91d1\u77ff\u50a8\u91cf(\u5428)',
        '\u6ed1\u77f3\u50a8\u91cf(\u4e07\u5428)',
        '\u539f\u751f\u949b\u94c1\u77ff\u50a8\u91cf(\u4e07\u5428)'
      ],
      selected: {},
      show: true,
      left: '10%',
      padding: 5,
      itemGap: 10,
      itemWidth: 25,
      itemHeight: 14,
      backgroundColor: 'transparent',
      borderColor: '#ccc',
      borderWidth: 1,
      borderRadius: 0,
      pageButtonItemGap: 5,
      pageButtonPosition: 'end',
      pageFormatter: '{current}/{total}',
      pageIconColor: '#2f4554',
      pageIconInactiveColor: '#aaa',
      pageIconSize: 15,
      animationDurationUpdate: 800,
      selector: false,
      selectorPosition: 'auto',
      selectorItemGap: 7,
      selectorButtonGap: 10
    }
  ],
  tooltip: {
    show: true,
    trigger: 'item',
    triggerOn: 'mousemove|click',
    axisPointer: {
      type: 'line'
    },
    showContent: true,
    alwaysShowContent: false,
    showDelay: 0,
    hideDelay: 100,
    enterable: false,
    confine: false,
    appendToBody: false,
    transitionDuration: 0.4,
    textStyle: {
      fontSize: 14
    },
    borderWidth: 0,
    padding: 5,
    order: 'seriesAsc'
  },
  title: [
    {
      show: true,
      text: '\u5404\u7c7b\u77ff\u4ea7\u50a8\u91cf',
      target: 'blank',
      subtext: '\u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40',
      subtarget: 'blank',
      padding: 5,
      itemGap: 10,
      textAlign: 'auto',
      textVerticalAlign: 'auto',
      triggerEvent: false
    }
  ]
})

let option3 = reactive({
  animation: true,
  animationThreshold: 2000,
  animationDuration: 1000,
  animationEasing: 'cubicOut',
  animationDelay: 0,
  animationDurationUpdate: 300,
  animationEasingUpdate: 'cubicOut',
  animationDelayUpdate: 0,
  aria: {
    enabled: false
  },
  color: [
    '#5470c6',
    '#91cc75',
    '#fac858',
    '#ee6666',
    '#73c0de',
    '#3ba272',
    '#fc8452',
    '#9a60b4',
    '#ea7ccc'
  ],
  series: [
    {
      type: 'pie',
      name: '\u6c34\u8d44\u6e90',
      colorBy: 'data',
      legendHoverLink: true,
      selectedMode: false,
      selectedOffset: 10,
      clockwise: true,
      startAngle: 90,
      minAngle: 0,
      minShowLabelAngle: 0,
      avoidLabelOverlap: true,
      stillShowZeroSum: true,
      percentPrecision: 2,
      showEmptyCircle: true,
      emptyCircleStyle: {
        color: 'lightgray',
        borderColor: '#000',
        borderWidth: 0,
        borderType: 'solid',
        borderDashOffset: 0,
        borderCap: 'butt',
        borderJoin: 'bevel',
        borderMiterLimit: 10,
        opacity: 1
      },
      data: [
        {
          name: '\u6c34\u8d44\u6e90\u603b\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '27088.1'
        },
        {
          name: '\u5730\u8868\u6c34\u8d44\u6e90\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '25984.4'
        },
        {
          name: '\u5730\u4e0b\u6c34\u8d44\u6e90\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '7924.4'
        },
        {
          name: '\u5730\u8868\u6c34\u4e0e\u5730\u4e0b\u6c34\u8d44\u6e90\u91cd\u590d\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '6820.7'
        },
        {
          name: '\u4eba\u5747\u6c34\u8d44\u6e90\u91cf(\u7acb\u65b9\u7c73/\u4eba)',
          value: '1918.2'
        }
      ],
      radius: ['0%', '75%'],
      center: ['58%', '50%'],
      label: {
        show: true,
        margin: 8,
        formatter: '{b}: {c}'
      },
      labelLine: {
        show: true,
        showAbove: false,
        length: 15,
        length2: 15,
        smooth: false,
        minTurnAngle: 90,
        maxSurfaceAngle: 90
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    }
  ],
  legend: [
    {
      data: [
        '\u6c34\u8d44\u6e90\u603b\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u5730\u8868\u6c34\u8d44\u6e90\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u5730\u4e0b\u6c34\u8d44\u6e90\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u5730\u8868\u6c34\u4e0e\u5730\u4e0b\u6c34\u8d44\u6e90\u91cd\u590d\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u4eba\u5747\u6c34\u8d44\u6e90\u91cf(\u7acb\u65b9\u7c73/\u4eba)'
      ],
      selected: {},
      show: true,
      left: '0%',
      top: '25%',
      orient: 'vertical',
      padding: 5,
      itemGap: 10,
      itemWidth: 25,
      itemHeight: 14,
      backgroundColor: 'transparent',
      borderColor: '#ccc',
      borderWidth: 1,
      borderRadius: 0,
      pageButtonItemGap: 5,
      pageButtonPosition: 'end',
      pageFormatter: '{current}/{total}',
      pageIconColor: '#2f4554',
      pageIconInactiveColor: '#aaa',
      pageIconSize: 15,
      animationDurationUpdate: 800,
      selector: false,
      selectorPosition: 'auto',
      selectorItemGap: 7,
      selectorButtonGap: 10
    }
  ],
  tooltip: {
    show: true,
    trigger: 'item',
    triggerOn: 'mousemove|click',
    axisPointer: {
      type: 'line'
    },
    showContent: true,
    alwaysShowContent: false,
    showDelay: 0,
    hideDelay: 100,
    enterable: false,
    confine: false,
    appendToBody: false,
    transitionDuration: 0.4,
    textStyle: {
      fontSize: 14
    },
    borderWidth: 0,
    padding: 5,
    order: 'seriesAsc'
  },
  title: [
    {
      show: true,
      text: '\u6c34\u8d44\u6e90\u5e74\u5ea6\u6570\u636e',
      target: 'blank',
      subtext: '\u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40',
      subtarget: 'blank',
      padding: 5,
      itemGap: 10,
      textAlign: 'auto',
      textVerticalAlign: 'auto',
      triggerEvent: false
    }
  ]
})
let option4 = reactive({
  animation: true,
  animationThreshold: 2000,
  animationDuration: 1000,
  animationEasing: 'cubicOut',
  animationDelay: 0,
  animationDurationUpdate: 300,
  animationEasingUpdate: 'cubicOut',
  animationDelayUpdate: 0,
  aria: {
    enabled: false
  },
  color: [
    '#5470c6',
    '#91cc75',
    '#fac858',
    '#ee6666',
    '#73c0de',
    '#3ba272',
    '#fc8452',
    '#9a60b4',
    '#ea7ccc'
  ],
  series: [
    {
      type: 'pie',
      name: '\u68ee\u6797\u8d44\u6e90',
      colorBy: 'data',
      legendHoverLink: true,
      selectedMode: false,
      selectedOffset: 10,
      clockwise: true,
      startAngle: 90,
      minAngle: 0,
      minShowLabelAngle: 0,
      avoidLabelOverlap: true,
      stillShowZeroSum: true,
      percentPrecision: 2,
      showEmptyCircle: true,
      emptyCircleStyle: {
        color: 'lightgray',
        borderColor: '#000',
        borderWidth: 0,
        borderType: 'solid',
        borderDashOffset: 0,
        borderCap: 'butt',
        borderJoin: 'bevel',
        borderMiterLimit: 10,
        opacity: 1
      },
      data: [
        {
          name: '\u6797\u4e1a\u7528\u5730\u9762\u79ef(\u4e07\u516c\u9877)',
          value: '32368.55'
        },
        {
          name: '\u68ee\u6797\u9762\u79ef(\u4e07\u516c\u9877)',
          value: '22044.62'
        },
        {
          name: '\u4eba\u5de5\u6797\u9762\u79ef(\u4e07\u516c\u9877)',
          value: '8003.10'
        },
        {
          name: '\u68ee\u6797\u8986\u76d6\u7387(%)',
          value: '23.0'
        },
        {
          name: '\u6d3b\u7acb\u6728\u603b\u84c4\u79ef\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '190.07'
        },
        {
          name: '\u68ee\u6797\u84c4\u79ef\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
          value: '175.60'
        }
      ],
      radius: ['0%', '75%'],
      center: ['58%', '50%'],
      label: {
        show: true,
        margin: 8,
        formatter: '{b}: {c}'
      },
      labelLine: {
        show: true,
        showAbove: false,
        length: 15,
        length2: 15,
        smooth: false,
        minTurnAngle: 90,
        maxSurfaceAngle: 90
      },
      rippleEffect: {
        show: true,
        brushType: 'stroke',
        scale: 2.5,
        period: 4
      }
    }
  ],
  legend: [
    {
      data: [
        '\u6797\u4e1a\u7528\u5730\u9762\u79ef(\u4e07\u516c\u9877)',
        '\u68ee\u6797\u9762\u79ef(\u4e07\u516c\u9877)',
        '\u4eba\u5de5\u6797\u9762\u79ef(\u4e07\u516c\u9877)',
        '\u68ee\u6797\u8986\u76d6\u7387(%)',
        '\u6d3b\u7acb\u6728\u603b\u84c4\u79ef\u91cf(\u4ebf\u7acb\u65b9\u7c73)',
        '\u68ee\u6797\u84c4\u79ef\u91cf(\u4ebf\u7acb\u65b9\u7c73)'
      ],
      selected: {},
      show: true,
      left: '0%',
      top: '25%',
      orient: 'vertical',
      padding: 5,
      itemGap: 10,
      itemWidth: 25,
      itemHeight: 14,
      backgroundColor: 'transparent',
      borderColor: '#ccc',
      borderWidth: 1,
      borderRadius: 0,
      pageButtonItemGap: 5,
      pageButtonPosition: 'end',
      pageFormatter: '{current}/{total}',
      pageIconColor: '#2f4554',
      pageIconInactiveColor: '#aaa',
      pageIconSize: 15,
      animationDurationUpdate: 800,
      selector: false,
      selectorPosition: 'auto',
      selectorItemGap: 7,
      selectorButtonGap: 10
    }
  ],
  tooltip: {
    show: true,
    trigger: 'item',
    triggerOn: 'mousemove|click',
    axisPointer: {
      type: 'line'
    },
    showContent: true,
    alwaysShowContent: false,
    showDelay: 0,
    hideDelay: 100,
    enterable: false,
    confine: false,
    appendToBody: false,
    transitionDuration: 0.4,
    textStyle: {
      fontSize: 14
    },
    borderWidth: 0,
    padding: 5,
    order: 'seriesAsc'
  },
  title: [
    {
      show: true,
      text: '\u68ee\u6797\u8d44\u6e90\u5e74\u5ea6\u6570\u636e',
      target: 'blank',
      subtext: '\u6570\u636e\u6765\u6e90\uff1a\u56fd\u5bb6\u7edf\u8ba1\u5c40',
      subtarget: 'blank',
      padding: 5,
      itemGap: 10,
      textAlign: 'auto',
      textVerticalAlign: 'auto',
      triggerEvent: false
    }
  ]
})

let option5 = reactive({
  animation: true,
  animationThreshold: 2000,
  animationDuration: 1000,
  animationEasing: 'cubicOut',
  animationDelay: 0,
  animationDurationUpdate: 300,
  animationEasingUpdate: 'cubicOut',
  animationDelayUpdate: 0,
  aria: {
    enabled: false
  },
  color: [
    '#5470c6',
    '#91cc75',
    '#fac858',
    '#ee6666',
    '#73c0de',
    '#3ba272',
    '#fc8452',
    '#9a60b4',
    '#ea7ccc'
  ],
  series: [
    {
      type: 'wordCloud',
      name: '\u4e2d\u5171\u4e8c\u5341\u5927\u62a5\u544a\u70ed\u8bcd',
      shape: 'circle',
      rotationRange: [-90, 90],
      rotationStep: 45,
      girdSize: 20,
      sizeRange: [6, 66],
      data: [
        {
          name: '\u4eba\u6c11',
          value: '177',
          textStyle: {
            color: 'rgb(3,142,134)'
          }
        },
        {
          name: '\u548c\u5e73',
          value: '22',
          textStyle: {
            color: 'rgb(135,115,68)'
          }
        },
        {
          name: '\u53f0\u6e7e',
          value: '13',
          textStyle: {
            color: 'rgb(152,153,15)'
          }
        },
        {
          name: '\u6c11\u751f',
          value: '15',
          textStyle: {
            color: 'rgb(15,71,45)'
          }
        },
        {
          name: '\u594b\u6597',
          value: '28',
          textStyle: {
            color: 'rgb(63,21,39)'
          }
        },
        {
          name: '\u81ea\u4fe1',
          value: '14',
          textStyle: {
            color: 'rgb(29,43,37)'
          }
        },
        {
          name: '\u65b0\u65f6\u4ee3',
          value: '39',
          textStyle: {
            color: 'rgb(90,159,28)'
          }
        },
        {
          name: '\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49',
          value: '42',
          textStyle: {
            color: 'rgb(108,95,83)'
          }
        },
        {
          name: '\u4e2d\u56fd\u5171\u4ea7\u515a',
          value: '29',
          textStyle: {
            color: 'rgb(78,27,147)'
          }
        },
        {
          name: '\u56fd\u5bb6',
          value: '138',
          textStyle: {
            color: 'rgb(17,51,16)'
          }
        },
        {
          name: '\u73b0\u4ee3\u5316',
          value: '86',
          textStyle: {
            color: 'rgb(107,34,56)'
          }
        },
        {
          name: '\u9a6c\u514b\u601d\u4e3b\u4e49',
          value: '29',
          textStyle: {
            color: 'rgb(18,2,56)'
          }
        },
        {
          name: '\u6c11\u65cf',
          value: '47',
          textStyle: {
            color: 'rgb(34,56,126)'
          }
        },
        {
          name: '\u6587\u5316',
          value: '58',
          textStyle: {
            color: 'rgb(113,81,38)'
          }
        },
        {
          name: '\u4e2d\u56fd',
          value: '180',
          textStyle: {
            color: 'rgb(111,80,90)'
          }
        },
        {
          name: '\u4e2d\u534e\u6c11\u65cf\u4f1f\u5927\u590d\u5174',
          value: '15',
          textStyle: {
            color: 'rgb(95,45,123)'
          }
        },
        {
          name: '\u6539\u9769\u5f00\u653e',
          value: '11',
          textStyle: {
            color: 'rgb(112,14,156)'
          }
        },
        {
          name: '\u4eba\u6c11',
          value: '177',
          textStyle: {
            color: 'rgb(136,144,136)'
          }
        },
        {
          name: '\u548c\u5e73',
          value: '22',
          textStyle: {
            color: 'rgb(57,124,90)'
          }
        },
        {
          name: '\u53f0\u6e7e',
          value: '13',
          textStyle: {
            color: 'rgb(1,114,6)'
          }
        },
        {
          name: '\u6c11\u751f',
          value: '15',
          textStyle: {
            color: 'rgb(49,7,54)'
          }
        },
        {
          name: '\u594b\u6597',
          value: '28',
          textStyle: {
            color: 'rgb(118,136,128)'
          }
        },
        {
          name: '\u81ea\u4fe1',
          value: '14',
          textStyle: {
            color: 'rgb(76,4,122)'
          }
        },
        {
          name: '\u65b0\u65f6\u4ee3',
          value: '39',
          textStyle: {
            color: 'rgb(50,133,99)'
          }
        },
        {
          name: '\u4e2d\u56fd\u7279\u8272\u793e\u4f1a\u4e3b\u4e49',
          value: '42',
          textStyle: {
            color: 'rgb(6,127,60)'
          }
        },
        {
          name: '\u4e2d\u56fd\u5171\u4ea7\u515a',
          value: '29',
          textStyle: {
            color: 'rgb(139,141,114)'
          }
        },
        {
          name: '\u56fd\u5bb6',
          value: '138',
          textStyle: {
            color: 'rgb(68,103,152)'
          }
        },
        {
          name: '\u73b0\u4ee3\u5316',
          value: '86',
          textStyle: {
            color: 'rgb(101,138,147)'
          }
        },
        {
          name: '\u9a6c\u514b\u601d\u4e3b\u4e49',
          value: '29',
          textStyle: {
            color: 'rgb(53,102,98)'
          }
        },
        {
          name: '\u6c11\u65cf',
          value: '47',
          textStyle: {
            color: 'rgb(35,148,128)'
          }
        },
        {
          name: '\u6587\u5316',
          value: '58',
          textStyle: {
            color: 'rgb(110,76,46)'
          }
        },
        {
          name: '\u4e2d\u56fd',
          value: '180',
          textStyle: {
            color: 'rgb(135,67,32)'
          }
        },
        {
          name: '\u4e2d\u534e\u6c11\u65cf\u4f1f\u5927\u590d\u5174',
          value: '15',
          textStyle: {
            color: 'rgb(40,112,24)'
          }
        },
        {
          name: '\u6539\u9769\u5f00\u653e',
          value: '11',
          textStyle: {
            color: 'rgb(133,5,52)'
          }
        }
      ],
      drawOutOfBound: false,
      textStyle: {
        emphasis: {}
      }
    }
  ],
  legend: [
    {
      data: [],
      selected: {},
      show: true,
      padding: 5,
      itemGap: 10,
      itemWidth: 25,
      itemHeight: 14,
      backgroundColor: 'transparent',
      borderColor: '#ccc',
      borderWidth: 1,
      borderRadius: 0,
      pageButtonItemGap: 5,
      pageButtonPosition: 'end',
      pageFormatter: '{current}/{total}',
      pageIconColor: '#2f4554',
      pageIconInactiveColor: '#aaa',
      pageIconSize: 15,
      animationDurationUpdate: 800,
      selector: false,
      selectorPosition: 'auto',
      selectorItemGap: 7,
      selectorButtonGap: 10
    }
  ],
  tooltip: {
    show: true,
    trigger: 'item',
    triggerOn: 'mousemove|click',
    axisPointer: {
      type: 'line'
    },
    showContent: true,
    alwaysShowContent: false,
    showDelay: 0,
    hideDelay: 100,
    enterable: false,
    confine: false,
    appendToBody: false,
    transitionDuration: 0.4,
    textStyle: {
      fontSize: 14
    },
    borderWidth: 0,
    padding: 5,
    order: 'seriesAsc'
  },
  title: [
    {
      show: true,
      text: '\u4e2d\u5171\u4e8c\u5341\u5927\u62a5\u544a\u70ed\u8bcd',
      target: 'blank',
      subtarget: 'blank',
      padding: 5,
      itemGap: 10,
      textAlign: 'auto',
      textVerticalAlign: 'auto',
      triggerEvent: false,
      textStyle: {
        fontSize: 23
      }
    }
  ]
})
// onMounted(async () => {
//   const res = await populationBarService()
//   delete res.data[0]
//   delete res.data[0]
//   option = res.data
// })
</script>
<template>
  <div :style="{ width: '100%', height: '37.4%' }">
    <Echarts :option="option1" />
  </div>

  <div
    :style="{
      width: '100%',
      height: '37.4%',
      borderTop: '1px solid black',
      borderBottom: '1px solid black'
    }"
  >
    <Echarts :option="option2" />
  </div>

  <div :style="{ width: '40%', height: '25%', float: 'left' }">
    <Echarts :option="option3" />
  </div>

  <div
    :style="{
      width: '40%',
      height: '25%',
      borderLeft: '1px solid black',
      borderRight: '1px solid black',
      float: 'left'
    }"
  >
    <Echarts :option="option4" />
  </div>

  <div :style="{ width: '19.9%', height: '25%', float: 'right' }">
    <Echarts :option="option5" />
  </div>
</template>

<!--<script setup>-->
<!--import { onMounted, onUnmounted } from 'vue'-->
<!--import * as echarts from 'echarts'-->
<!--let echart = echarts-->
<!--onMounted(() => {-->
<!--  initChart()-->
<!--})-->
<!--onUnmounted(() => {-->
<!--  echart.dispose()-->
<!--})-->
<!--function initChart() {-->
<!--  let chart = echart.init(document.getElementById('myEcharts'), 'dark')-->
<!--  // 把配置和数据放这里-->
<!--  chart.setOption({-->
<!--    xAxis: {-->
<!--      type: 'category',-->
<!--      data: [-->
<!--        '一月',-->
<!--        '二月',-->
<!--        '三月',-->
<!--        '四月',-->
<!--        '五月',-->
<!--        '六月',-->
<!--        '七月',-->
<!--        '八月',-->
<!--        '九月',-->
<!--        '十月',-->
<!--        '十一月',-->
<!--        '十二月'-->
<!--      ]-->
<!--    },-->
<!--    tooltip: {-->
<!--      trigger: 'axis'-->
<!--    },-->
<!--    yAxis: {-->
<!--      type: 'value'-->
<!--    },-->
<!--    series: [-->
<!--      {-->
<!--        data: [820, 932, 901, 934, 1290, 1330, 1320, 801, 102, 230, 4321, 4129],-->
<!--        type: 'line',-->
<!--        smooth: true-->
<!--      }-->
<!--    ]-->
<!--  })-->
<!--  window.onresize = function () {-->
<!--    //自适应大小-->
<!--    chart.resize()-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--  <div class="echarts-box">-->
<!--    <div id="myEcharts" :style="{ width: '900px', height: '300px' }"></div>-->
<!--  </div>-->
<!--</template>-->

<!--<style scoped></style>-->
