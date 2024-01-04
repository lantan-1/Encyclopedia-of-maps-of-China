from pyecharts import options as opts
from pyecharts.charts import Funnel
from csv_to_others import csv_to_others

c = (
    Funnel()
    .add(
        "矿产储量",
        [[csv_to_others().mining_csv_to_list()[0][i], csv_to_others().mining_csv_to_list()[1][i]] for i in range(len(csv_to_others().mining_csv_to_list()[0]))],
        sort_="ascending",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="各类矿产储量",subtitle="数据来源：国家统计局"),
                     legend_opts=opts.LegendOpts(pos_left='10%'))
    # .render("funnel_sort_ascending.html")
)
population_bar_options = c.dump_options_with_quotes()
print(population_bar_options)