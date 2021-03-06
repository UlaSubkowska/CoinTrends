from app import app
from flask import render_template
from app.forms import GetDate
from app.logic import get_prices,data_for_chart_labels, data_for_chart_prices, week_annotation, divide_data, \
    trends_lines, grow_drop, BTCUSD_relations


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = GetDate()
    if form.validate_on_submit():
        start_date = str(form.start_date)[-12:-2]
        end_date = str(form.end_date)[-12:-2]
        trends=form.trends.data

        if trends:
            labels = data_for_chart_labels(get_prices('BTCUSD', start_date, end_date))
            BTCUSD = data_for_chart_prices(get_prices('BTCUSD', start_date, end_date))
            ETHUSD = data_for_chart_prices(get_prices('ETHUSD', start_date, end_date))
            LTCUSD = data_for_chart_prices(get_prices('LTCUSD', start_date, end_date))

            week, amount=week_annotation(labels)
            B_trends=trends_lines(divide_data(BTCUSD))
            E_trends=trends_lines(divide_data(ETHUSD))
            L_trends=trends_lines(divide_data(LTCUSD))

            trend_message=BTCUSD_relations(grow_drop(B_trends),grow_drop(E_trends),grow_drop(L_trends))
            B_grow_drop= grow_drop(B_trends)
            del B_grow_drop[-1]

            return render_template('chart_with_trend.html', labels=labels, BTCUSD=BTCUSD, ETHUSD=ETHUSD, LTCUSD=LTCUSD,
                                   week=week, amount=amount, B_trends=B_trends, E_trends=E_trends, L_trends=L_trends,
                                   trend_message=trend_message, B_grow_drop=B_grow_drop)

        labels=data_for_chart_labels(get_prices('BTCUSD', start_date, end_date))
        BTCUSD=data_for_chart_prices(get_prices('BTCUSD', start_date, end_date))
        ETHUSD=data_for_chart_prices(get_prices('ETHUSD', start_date, end_date))
        LTCUSD=data_for_chart_prices(get_prices('LTCUSD', start_date, end_date))

        return render_template('chart.html', labels=labels, BTCUSD=BTCUSD, ETHUSD=ETHUSD, LTCUSD=LTCUSD)
    return render_template('index.html', form=form)

