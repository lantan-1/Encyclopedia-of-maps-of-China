from pyecharts import options as opts
from pyecharts.charts import WordCloud
from csv_to_others import csv_to_others

c=(
    WordCloud()
    .add(series_name="中共二十大报告热词", data_pair=csv_to_others().report_csv_to_list(), word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="中共二十大报告热词", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    # .render("basic_wordcloud.html")
)
report_wordcloud_options = c.dump_options_with_quotes()
print(report_wordcloud_options)