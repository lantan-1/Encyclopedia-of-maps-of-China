import request from '@/utils/request'

// 注册接口
export const userRegisterService = ({ username, password, repassword }) =>
  request.post('/app01/register/', { username, password, repassword })

// 登录接口
export const userLoginService = ({ username, password }) =>
  request.post('/app01/login/', { username, password })

// 修改密码接口
export const userChgPwdService = ({ username, oldpassword, password, repassword }) =>
    request.post('/app01/chgpwd/', { username, oldpassword, password, repassword })

// 注销接口
export const userDestroyService = ({ username, password, repassword }) =>
    request.post('/app01/destroy/', { username, password, repassword })

// 获取用户基本信息
export const userGetInfoService = () => request.get('/my/userinfo')

// 更新用户基本信息
export const userUpdateInfoService = ({ id, nickname, email }) =>
  request.put('/my/userinfo', { id, nickname, email })

// 更新用户头像
export const userUpdateAvatarService = (avatar) =>
  request.patch('/my/update/avatar', { avatar })

// 更新用户密码
export const userUpdatePasswordService = ({ old_pwd, new_pwd, re_pwd }) =>
  request.patch('/my/updatepwd', { old_pwd, new_pwd, re_pwd })
