import json

from flask import (
	Flask,
	Response,
	render_template,
	url_for,
	redirect,
	request,
	session,
	jsonify,
	send_file
)

# import pandas as pd
# import numpy as np

# import plotly
# import plotly.graph_objs as go


app = Flask(__name__)


# def plot_two_bedrooms_price_by_outwward_code():
# 	plot_df = pd.read_csv('./static/data/onthemarket_clean_data.csv')

# 	plot_df = (
# 		plot_df
# 		.loc[:, ['outward_code', 'bedrooms', 'price_extracted']]
# 		.groupby(['outward_code', 'bedrooms']).agg(
# 			price = pd.NamedAgg('price_extracted', 'mean')
# 		)
# 		.reset_index()
# 		.sort_values(by='price')
# 	)

# 	plot_df = plot_df.loc[plot_df['bedrooms'] == 2, ['outward_code', 'price']]

# 	x = plot_df['outward_code']
# 	y = plot_df['price']

# 	plot_df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

# 	bar = go.Bar(
# 			x=x, # assign x as the dataframe column 'x'
# 			y=y
# 		)

# 	fig = go.Figure()

# 	fig.add_trace(bar)
# 	fig.update_layout(
# 		title="New Builds - 2 Bedroom",
# 		xaxis_title="Outward Code",
# 		yaxis_title="Price",
# 	)

# 	return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# def plot_test():
# 	N = 40
# 	x = np.linspace(0, 1, N)
# 	y = np.random.randn(N)
# 	df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

# 	data = [
# 		go.Bar(
# 			x=df['x'], # assign x as the dataframe column 'x'
# 			y=df['y']
# 		)
# 	]

# 	return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')


# @app.route('/about')
# def about():
# 	return render_template('about.html', title='About')


# @app.route('/analytics')
# def analytics():
# 	return render_template('analytics.html', title='Analytics')

# 	bar = plot_two_bedrooms_price_by_outwward_code()
# 	return render_template('analytics.html', plot=bar, title='Analytics')


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=3000)





