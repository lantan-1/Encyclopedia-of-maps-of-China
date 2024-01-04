<template>
  <label
    >中心点经度：<el-input
      style="width: 100px"
      v-model.number="center.lng"
      placeholder="请输入..." /></label
  >&nbsp;&nbsp;&nbsp;
  <label
    >中心点纬度：<el-input
      style="width: 100px"
      v-model.number="center.lat"
      placeholder="请输入..." /></label
  >&nbsp;&nbsp;&nbsp;
  <label
    >缩放比例：<el-input
      style="width: 100px"
      v-model.number="zoom"
      placeholder="请输入..." /></label
  >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <span>{{
    '当前位置：' +
    center.longitude +
    ':' +
    Math.abs(center.lng) +
    '° ' +
    center.latitude +
    ':' +
    Math.abs(center.lat) +
    '°'
  }}</span>
  <el-button
    @click="
      center.lng = 117.32208859741814;
      center.lat = 38.39078991888;
      zoom = 17;
    "
    style="float: right"
    size="small"
    type="primary"
    plain
    >沧州交通学院</el-button
  >
  <baidu-map
    class="map"
    :scroll-wheel-zoom="true"
    :center="center"
    :zoom="zoom"
    @moving="syncCenterAndZoom"
    @moveend="syncCenterAndZoom"
    @zoomend="syncCenterAndZoom"
  >
    <bm-map-type
      :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']"
      anchor="BMAP_ANCHOR_TOP_LEFT"
    ></bm-map-type>
    <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
    <bm-scale anchor="BMAP_ANCHOR_BOTTOM_LEFT"></bm-scale>
  </baidu-map>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const center = ref({
  lng: 112.8,
  lat: 37.6,
  longitude: '东经E',
  latitude: '北纬N'
})

let zoom = ref(9)

const syncCenterAndZoom = (e) => {
  const { lng, lat } = e.target.getCenter()
  zoom.value = e.target.getZoom()
  nextTick(() => {
    center.value.lng = lng
    center.value.lat = lat
    if (center.value.lng > 0) center.value.longitude = '东经E'
    else center.value.longitude = '西经W'
    if (center.value.lat > 0) center.value.latitude = '北纬N'
    else center.value.latitude = '南纬S'
  })
}
</script>
<style scoped>
.map {
  width: 100%;
  height: 85vh;
}
</style>
