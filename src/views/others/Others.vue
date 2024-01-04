<template>
  <div class="demo-collapse">
    <el-collapse v-model="activeNames" @change="handleChange" accordion>
      <el-collapse-item title="&nbsp;&nbsp;&nbsp;&nbsp;🥰Vue 3" name="1">
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;Vue 3</h2>
        <h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;渐进式 JavaScript 框架</h4>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;易学易用，性能出色，适用场景丰富的 Web 前端框架。
        </div>
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;易学易用</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;基于标准 HTML、CSS 和 JavaScript 构建，提供容易上手的 API 和一流的文档。
        </div>
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;性能出色</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;经过编译器优化、完全响应式的渲染系统，几乎不需要手动优化。
        </div>
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;灵活多变</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;丰富的、可渐进式集成的生态系统，可以根据应用规模在库和框架间切换自如。
        </div>

      </el-collapse-item>
      <el-collapse-item title="&nbsp;&nbsp;&nbsp;&nbsp;🥰Django 5" name="2">
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;Django 5</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django 是一个用于构建 Web 应用程序的高级 Python Web 框架。
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django 提供了一套强大的工具和约定，使得开发者能够快速构建功能齐全且易于维护的网站。
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django 采用了 MVT 的软件设计模式，即模型（Model），视图（View）和模板（Template）。
        </div>

        <h2>&nbsp;&nbsp;&nbsp;&nbsp;模型层¶</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django 提供了一个抽象的模型（“models”）层，用于结构化和操作你的网页应用程序的数据。
        </div>

        <h2>&nbsp;&nbsp;&nbsp;&nbsp;视图层¶</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Django 具有 “视图” 的概念，负责处理用户的请求并返回响应。通过以下链接查找所有你需要知道的有关视图的信息：
        </div>

        <h2>&nbsp;&nbsp;&nbsp;&nbsp;模板层¶</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模板层提供了一个对设计者友好的语法用于渲染向用户呈现的信息。学习如何使用语法（面向设计者）以及如何扩展（面向程序员）：
        </div>
      </el-collapse-item>
      <el-collapse-item title="&nbsp;&nbsp;&nbsp;&nbsp;🥰ECharts" name="3">
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;ECharts</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个使用 JavaScript 实现的开源可视化库，可以流畅的运行在 PC
          和移动设备上，兼容当前绝大部分浏览器（IE9/10/11，Chrome，Firefox，Safari等），底层依赖矢量图形库
          ZRender，提供直观，交互丰富，可高度个性化定制的数据可视化图表。
        </div>

        <h2>
          &nbsp;&nbsp;&nbsp;&nbsp;丰富的可视化类型
        </h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ECharts 提供了常规的折线图、柱状图、散点图、饼图、K线图，用于统计的盒形图，用于地理数据可视化的地图、热力图、线图，用于关系数据可视化的关系图、treemap、旭日图，多维数据可视化的平行坐标，还有用于
          BI 的漏斗图，仪表盘，并且支持图与图之间的混搭。
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;除了已经内置的包含了丰富功能的图表，ECharts
          还提供了自定义系列，只需要传入一个renderItem函数，就可以从数据映射到任何你想要的图形，更棒的是这些都还能和已有的交互组件结合使用而不需要操心其它事情。
        </div>

        <h2>
          &nbsp;&nbsp;&nbsp;&nbsp;多种数据格式无需转换直接使用
        </h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ECharts 内置的 dataset 属性（4.0+）支持直接传入包括二维表，key-value 等多种格式的数据源，通过简单的设置 encode
          属性就可以完成从数据到图形的映射，这种方式更符合可视化的直觉，省去了大部分场景下数据转换的步骤，而且多个组件能够共享一份数据而不用克隆。
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了配合大数据量的展现，ECharts 还支持输入 TypedArray 格式的数据，TypedArray 在大数据量的存储中可以占用更少的内存，对
          GC 友好等特性也可以大幅度提升可视化应用的性能。
        </div>

        <h2>
          &nbsp;&nbsp;&nbsp;&nbsp;多渲染方案，跨平台使用！
        </h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ECharts 支持以 Canvas、SVG（4.0+）、VML 的形式渲染图表。VML 可以兼容低版本 IE，SVG 使得移动端不再为内存担忧，Canvas
          可以轻松应对大数据量和特效的展现。不同的渲染方式提供了更多选择，使得 ECharts 在各种场景下都有更好的表现。
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;除了 PC 和移动端的浏览器，ECharts 还能在 node 上配合 node-canvas 进行高效的服务端渲染（SSR）。从 4.0
          开始我们还和微信小程序的团队合作，提供了 ECharts 对微信小程序的适配！
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;社区热心的贡献者也为我们提供了丰富的其它语言扩展，比如 Python 的 pyecharts，R 语言的 echarty, Julia 的
          ECharts.jl 等等。
        </div>
      </el-collapse-item>
      <el-collapse-item title="&nbsp;&nbsp;&nbsp;&nbsp;🥰Pyecharts" name="4">
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;Pyecharts</h2>
        <h2>&nbsp;&nbsp;&nbsp;&nbsp;Python Echarts 绘图库。</h2>
        <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;图表：30+种图表
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;地图：300+中国城市/200+国家和地区
          <br/>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;平台：纯 Python / Jupyter Notebook / Web 框架
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
  <el-carousel :interval="1000" type="card" height="220px">
    <el-carousel-item>
      <img src="@/assets/VueLogo.jpg" alt="VueLogo" style="height: 200px;width: 450px">
    </el-carousel-item>
    <el-carousel-item>
      <img src="@/assets/DjangoLogo.jpg" alt="DjangoLogo" style="height: 200px;width: 450px">
    </el-carousel-item>
    <el-carousel-item>
      <img src="@/assets/Echarts.jpg" alt="Echarts" style="height: 200px;width: 450px">
    </el-carousel-item>
    <el-carousel-item>
      <img src="@/assets/Pyecharts.jpg" alt="Pyecharts" style="height: 200px;width: 450px">
    </el-carousel-item>
    <el-carousel-item>
      <img src="@/assets/HTML_JS_CSS_Logo.jpg" alt="HTML_JS_CSS_Logo" style="height: 200px;width: 450px">
    </el-carousel-item>
    <el-carousel-item>
      <img src="@/assets/PythonLogo.webp" alt="PythonLogo" style="height: 200px;width: 450px">
    </el-carousel-item>
  </el-carousel>
</template>

<script lang="ts" setup>
import {ref} from 'vue'

const activeNames = ref(['1'])
const handleChange = (val: string[]) => {
  console.log(val)
}
</script>

<style scoped>

</style>
