<script lang="ts" setup>
import { ref, watch } from 'vue'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting
} from '@element-plus/icons-vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()
const isCollapse = ref(false)
const user = ref(userStore.user)
const logout = () => {
  ElMessageBox.confirm('你确认要进行退出么', '温馨提示', {
    type: 'warning',
    confirmButtonText: '确定',
    cancelButtonText: '取消'
  })
    .then(() => {
      userStore.removeToken()
      userStore.setUser({})
      router.push('/')
      ElMessage({
        type: 'success',
        message: '退出登录'
      })
    })
    .catch(() => {})
}

watch(
  () => route.path,
  (newPath, oldPath) => {
    if (newPath === '/knowledge') isCollapse.value = true
    if (oldPath === '/knowledge') isCollapse.value = false
  },
  { immediate: true, deep: true }
)
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-menu
          style="padding: 0"
          :default-active="$route.path"
          class="el-menu-demo"
          mode="horizontal"
          :ellipsis="false"
        >
          <el-menu-item index="0" @click="router.push('/maps/china')">
            <img
              style="width: 70px"
              src="@/assets/logo.svg"
              alt="Element logo"
            />
            <h3 style="color: #409eff">中国地图网</h3>
          </el-menu-item>
          <div class="flex-grow" />
          <el-menu-item index="1" @click="isCollapse = !isCollapse"
            >切换
          </el-menu-item>
          <el-menu-item index="2" @click="logout">退出登录</el-menu-item>
          <el-sub-menu index="3" style="width: 100px">
            <template #title>{{ user[0]['user_name'] }}</template>
            <el-menu-item index="3-1" @click="router.push('/user')"
              >用户信息
            </el-menu-item>
            <el-menu-item index="3-2" @click="router.push('/user/chgpwd')"
              >修改密码
            </el-menu-item>
            <el-menu-item index="3-3" @click="router.push('/user/destroy')"
              >注销账户
            </el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-header>

      <el-container>
        <el-aside width="auto">
          <el-menu
            default-active="$route.path"
            class="el-menu-vertical-demo"
            :collapse="isCollapse"
          >
            <el-sub-menu index="1">
              <template #title @click="router.push('/maps/china')">
                <el-icon @click="router.push('/maps/china')">
                  <Location />
                </el-icon>
                <span @click="router.push('/maps/china')">中国地图</span>
              </template>
              <el-menu-item index="1-2" @click="router.push('/maps/hebei')"
                >河北省地图
              </el-menu-item>
              <el-menu-item index="1-3" @click="router.push('/maps/henan')"
                >河南省地图
              </el-menu-item>
              <el-menu-item index="1-4" @click="router.push('/maps/shandong')"
                >山东省地图
              </el-menu-item>
              <el-menu-item index="1-5" @click="router.push('/maps/shanxi')"
                >山西省地图
              </el-menu-item>
            </el-sub-menu>

            <el-menu-item index="2" @click="router.push('/knowledge')">
              <el-icon>
                <document />
              </el-icon>
              <template #title>地理知识</template>
            </el-menu-item>

            <el-menu-item index="3" @click="router.push('/settings')">
              <el-icon>
                <setting />
              </el-icon>
              <template #title>设置</template>
            </el-menu-item>

            <el-menu-item index="4" @click="router.push('/others')">
              <el-icon>
                <IconMenu />
              </el-icon>
              <template #title>其他</template>
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
.flex-grow {
  flex-grow: 1;
}

.common-layout {
  height: 100vh;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 175px;
  height: 93vh;
}

.el-menu-vertical-demo:is(.el-menu--collapse) {
  width: 64px;
  height: 93vh;
}

.el-header {
  padding: 0;
}
</style>
