import pandas as pd
import plotly.express as px

def to_function(country):
    data = pd.read_csv(f'./data/{country}/unemployment-rate-imf.csv')
    data = data.rename(columns={
        'Unemployment rate - Percent of total labor force - Observations': 'Unemployment Rate'
    })
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    data['Unemployment Rate'] = data['Unemployment Rate'].astype(float)
    data['Year'] = data['Year'].dt.year
    return data

def to_function_all_countries(data, start_year, end_year):
    data = pd.read_csv(data)
    data = data.rename(columns={
        'Unemployment rate - Percent of total labor force - Observations': 'Unemployment Rate'
    })
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    data['Unemployment Rate'] = data['Unemployment Rate'].astype(float)
    data['Year'] = data['Year'].dt.year
    data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]
    return data

def plot_country_unemployment_rate_interactive(data):
    fig = px.line(
        data,
        x='Year',
        y='Unemployment Rate',
        title='Unemployment Rate in {} (1991-2021)'.format(data['Entity'].iloc[0]),
        labels={'Year': 'Year', 'Unemployment Rate': 'Unemployment Rate (%)'}
    )
    fig.update_layout(
        width=1200,
        height=700
    )
    fig.show(renderer="browser")
    # Cria um arquivo HTML
    # fig.write_html("Plot.html")

def plot_unemployment_all_countries_interactive(data):
    fig = px.line(
        data,
        x='Year',
        y='Unemployment Rate',
        color='Entity',
        title='Unemployment Rate by Country (1991-2021)'
    )
    fig.update_layout(
        legend=dict(
            title='Country',
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=1,
            font=dict(size=10),
            bgcolor='rgba(0,0,0,0)',
            bordercolor='Black',
            borderwidth=1
        ),
        width=1200,
        height=700
    )
    fig.show(renderer="browser")
    # Cria um arquivo HTML
    # fig.write_html("Plot.html")

# Exemplo de uso:

# Cada país
#plot_country_unemployment_rate_interactive(to_function('01 - switzerland'))
#plot_country_unemployment_rate_interactive(to_function('02 - norway'))
#plot_country_unemployment_rate_interactive(to_function('03 - iceland'))
#plot_country_unemployment_rate_interactive(to_function('04 - hongkong'))
#plot_country_unemployment_rate_interactive(to_function('05 - sweden'))
#plot_country_unemployment_rate_interactive(to_function('06 - germany'))
#plot_country_unemployment_rate_interactive(to_function('07 - ireland'))
#plot_country_unemployment_rate_interactive(to_function('08 - australia'))
#plot_country_unemployment_rate_interactive(to_function('09 - netherlands'))
#plot_country_unemployment_rate_interactive(to_function('10 - denmark'))
#plot_country_unemployment_rate_interactive(to_function('84 - brazil'))

# Todos os países desde 1980 (Alterar os valores dentro do parâmetro da função)
plot_unemployment_all_countries_interactive(to_function_all_countries('./data/all countries/unemployment-rate-imf.csv', 1980, 2021))