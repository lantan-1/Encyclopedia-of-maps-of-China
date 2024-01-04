<script setup>
import { Edit, View, Hide } from '@element-plus/icons-vue'
import { useUserStore } from '@/stores'
import { ref } from 'vue'
const userStore = useUserStore()
const user = ref(userStore.user)
let flag = ref(true)

const edit = () => {
  ElMessage({
    showClose: true,
    message: '权限不足，请联系管理员！Wechat：lantanyyds',
    type: 'warning'
  })
}
</script>

<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h3>用户信息与设置😘</h3>
        <el-button type="primary" :icon="Edit" plain @click="edit"></el-button>
      </div>
    </template>
    <div class="text item"><b>用户级别：</b>普通用户</div>
    <div class="text item">
      <b>用户&nbsp;I&nbsp;D&nbsp;：</b>{{ user[0]['user_id'] }}
    </div>
    <div class="text item"><b>用户昵称：</b>{{ user[0]['user_name'] }}</div>
    <div class="text item" v-if="flag">
      <b>用户密码：</b>************
      <el-icon
        @click="flag = !flag"
        size="18"
        style="cursor: pointer; position: absolute; left: 370px"
        ><Hide
      /></el-icon>
    </div>
    <div class="text item" v-else>
      <b>用户密码：</b>{{ user[0]['user_pwd'] }}
      <el-icon
        @click="flag = !flag"
        size="18"
        style="cursor: pointer; position: absolute; left: 370px"
        ><View
      /></el-icon>
    </div>
    <template #footer>到此为止吧，😎不想写了</template>
  </el-card>
  <el-empty :image-size="350"> </el-empty>
</template>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>
