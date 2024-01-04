from pyecharts import options as opts
from pyecharts.charts import Pie
from csv_to_others import csv_to_others

c = (
    Pie()
    .add("水资源",
         [[csv_to_others().water_csv_to_list()[0][i], csv_to_others().water_csv_to_list()[1][i]] for i in range(len(csv_to_others().water_csv_to_list()[0]))])
    .set_global_opts(title_opts=opts.TitleOpts(title="水资源年度数据",subtitle="数据来源：国家统计局"),
                     legend_opts=opts.LegendOpts(pos_left='0%',pos_top='25%',orient='vertical'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"),
                     )
    # .render("pie_water.html")
)
water_bar_options = c.dump_options_with_quotes()
print(water_bar_options)