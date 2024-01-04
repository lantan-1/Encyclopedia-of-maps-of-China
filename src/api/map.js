import request from '@/utils/request'

// 获取中国地图chart_options
export const mapChinaService = () => request.get('/app01/china/')
// 获取河北地图chart_options
export const mapHeBeiService = () => request.get('/app01/hebei/')
// 获取河南地图chart_options
export const mapHeNanService = () => request.get('/app01/henan/')
// 获取山东地图chart_options
export const mapShanDongService = () => request.get('/app01/shandong/')
// 获取山西地图chart_options
export const mapShanXiService = () => request.get('/app01/shanxi/')


// 获取人口柱状图population_bar_options
export const populationBarService = () => request.get('/app01/population_bar/')
