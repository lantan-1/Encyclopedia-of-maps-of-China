<script setup>
import { userChgPwdService } from '@/api/user.js'
import { User, Lock } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { useUserStore } from '@/stores'
import { useRouter } from 'vue-router'
const form = ref()

// 整个的用于提交的form数据对象
const formModel = ref({
  username: '',
  oldpassword: '',
  password: '',
  repassword: ''
})
const rules = {
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 3, max: 20, message: '用户名必须是 3-20位 的字符', trigger: 'blur' }
  ],
  oldpassword: [
    { required: true, message: '请输入旧密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是 6-15位 的非空字符',
      trigger: 'blur'
    }
  ],
  password: [
    { required: true, message: '请输入新密码', trigger: 'blur' },
    {
      pattern: /^\S{6,15}$/,
      message: '密码必须是 6-15位 的非空字符',
      trigger: 'blur'
    }
  ],
  repassword: [
    { required: true, message: '请再次输入新密码', trigger: 'blur' },
    {
      pattern: /^\S{6,20}$/,
      message: '密码必须是6-20位的非空字符',
      trigger: 'blur'
    },
    {
      validator: (rule, value, callback) => {
        // 判断 value 和 当前 form 中收集的 password 是否一致
        if (value !== formModel.value.password) {
          callback(new Error('两次输入密码不一致'))
        } else {
          callback() // 就算校验成功，也需要callback
        }
      },
      trigger: 'blur'
    }
  ]
}
const router = useRouter()
const userStore = useUserStore()
const chgpwd = async () => {
  await form.value.validate()
  await userChgPwdService(formModel.value)
  userStore.removeToken()
  userStore.setUser({})
  userStore.setUserName('')
  router.push('/')
  ElMessage.success('修改密码成功，请重新登录！')
}
</script>

<template>
  <el-form
    :model="formModel"
    :rules="rules"
    ref="form"
    size="large"
    autocomplete="off"
    style="width: 30%"
  >
    <el-form-item>
      <h1>修改密码😉</h1>
    </el-form-item>
    <el-form-item prop="username">
      <el-input
        v-model="formModel.username"
        :prefix-icon="User"
        placeholder="请输入用户名"
      ></el-input>
    </el-form-item>
    <el-form-item prop="oldpassword">
      <el-input
        v-model="formModel.oldpassword"
        :prefix-icon="Lock"
        type="password"
        placeholder="请输入旧密码"
      ></el-input>
    </el-form-item>
    <el-form-item prop="password">
      <el-input
        v-model="formModel.password"
        :prefix-icon="Lock"
        type="password"
        placeholder="请输入新密码"
      ></el-input>
    </el-form-item>
    <el-form-item prop="repassword">
      <el-input
        v-model="formModel.repassword"
        :prefix-icon="Lock"
        type="password"
        placeholder="请再次输入新密码"
      ></el-input>
    </el-form-item>
    <el-form-item>
      <el-button
        @click="formModel = {}"
        class="button"
        auto-insert-space
        style="width: 48.1%"
      >
        重置
      </el-button>
      <el-button
        @click="chgpwd"
        class="button"
        type="primary"
        auto-insert-space
        style="width: 48.1%"
      >
        提交
      </el-button>
    </el-form-item>
  </el-form>

  <el-empty :image-size="350"> </el-empty>
</template>

<style lang="scss" scoped>
.login-page {
  height: 100vh;
  background-color: #fff;
  .bg {
    background: url('@/assets/globe_1920_opacity.jpg') no-repeat center / cover;
    border-radius: 0 20px 20px 0;
  }
  .form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    user-select: none;
    .title {
      margin: 0 auto;
    }
    .button {
      width: 100%;
    }
    .flex {
      width: 100%;
      display: flex;
      justify-content: space-between;
    }
  }
}
</style>
