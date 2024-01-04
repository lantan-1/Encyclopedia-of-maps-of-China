from pyecharts import options as opts
from pyecharts.charts import Bar
from csv_to_others import csv_to_others

class population_bar:
    def population_bar_echarts(self):
        c = (
            Bar(init_opts=opts.InitOpts(width="1350px"))
            .add_xaxis(csv_to_others().population_csv_to_list()[1])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][0], csv_to_others().population_csv_to_list()[2][9])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][1], csv_to_others().population_csv_to_list()[2][8])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][2], csv_to_others().population_csv_to_list()[2][7])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][3], csv_to_others().population_csv_to_list()[2][6])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][4], csv_to_others().population_csv_to_list()[2][5])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][5], csv_to_others().population_csv_to_list()[2][4])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][6], csv_to_others().population_csv_to_list()[2][3])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][7], csv_to_others().population_csv_to_list()[2][2])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][8], csv_to_others().population_csv_to_list()[2][1])
            .add_yaxis(csv_to_others().population_csv_to_list()[0][9], csv_to_others().population_csv_to_list()[2][0])
            .set_global_opts(title_opts=opts.TitleOpts(title="近十年各省总人口"),
                             xaxis_opts=opts.AxisOpts(name="数据来源：国家统计局",
                                                      axislabel_opts=opts.LabelOpts(rotate=-35)),
                             yaxis_opts=opts.AxisOpts(name="单位：万人"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .render("bar_base.html")
        )
        population_bar_options = c.dump_options_with_quotes()
        print(population_bar_options)
        return population_bar_options
population_bar().population_bar_echarts()