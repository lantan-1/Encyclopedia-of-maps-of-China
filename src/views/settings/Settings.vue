<template>
  <el-calendar ref="calendar">
    <template #header="{ date }" #date-cell="{ date }">
      <el-button type="primary" @click="open" plain>备忘录</el-button>
      <h2>{{ date }}</h2>
      <el-button-group>
        <el-button size="large" @click="selectDate('prev-year')">
          ⋘⋘
        </el-button>
        <el-button size="large" @click="selectDate('prev-month')">
          ⋘
        </el-button>
        <el-button size="large" color="red" @click="selectDate('today')">今</el-button>
        <el-button size="large" @click="selectDate('next-month')">
          ⋙
        </el-button>
        <el-button size="large" @click="selectDate('next-year')">
          ⋙⋙
        </el-button>
      </el-button-group>
    </template>
  </el-calendar>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import type { CalendarDateType, CalendarInstance } from 'element-plus'

const calendar = ref<CalendarInstance>()
const selectDate = (val: CalendarDateType) => {
  if (!calendar.value) return
  calendar.value.selectDate(val)
}
const open = () => {
  ElMessageBox.prompt('我也不知道该写点啥了🤣', '请输入', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    inputErrorMessage: 'Error！！！',
  })
      .then(({ value }) => {
        ElMessage({
          type: 'success',
          message: `事件为:${value}`,
        })
      })
      .catch(() => {
        ElMessage({
          type: 'info',
          message: '已取消',
        })
      })
}
</script>
<style scoped>

</style>
