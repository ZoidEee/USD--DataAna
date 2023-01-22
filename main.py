import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

maticData = pd.read_excel('Matic.xlsx')
optimismData = pd.read_excel('Optimism.xlsx')
binanceData = pd.read_excel('Binance.xlsx')
avalancheData = pd.read_excel('Avalanche.xlsx')
mPay = [s.split('$')[1] for s in maticData['Amount']]
oPay = [s.split('$')[1] for s in optimismData['Amount']]
bPay = [s.split('$')[1] for s in binanceData['Amount']]
aPay = [s.split('$')[1] for s in avalancheData['Amount']]
oDates = list(optimismData['Date'])
mDates = list(maticData['Date'])
bDates = list(binanceData['Date'])
aDates = list(avalancheData['Date'])
oAPYdata = [line[:-1] for line in list(optimismData['APY'])]
mAPYdata = [line[:-1] for line in list(maticData['APY'])]
bAPYdata = [line[:-1] for line in list(binanceData['APY'])]
aAPYdata = [line[:-1] for line in list(avalancheData['APY'])]

option = ['O', 'M', 'B', 'A']
times = ['D', 'B', 'M']


# div_payment = []

def estimate(amount, network):
    holdings = amount

    mL = []

    if network == option[0]:
        for line in oPay:
            holdings = holdings * float(line) + holdings
            print(line)
            mL.append(holdings)
        return mL
    elif network == option[1]:
        for line in mPay:
            print(line)

            holdings = holdings * float(line) + holdings
            mL.append(holdings)
        return mL
    elif network == option[2]:
        for line in bPay:
            print(line)

            holdings = holdings * float(line) + holdings
            mL.append(holdings)
        return mL
    elif network == option[3]:
        for line in aPay:
            print(line)
            holdings = holdings * float(line) + holdings
            print()
            mL.append(holdings)
        return mL

    elif network != any(option):
        print(f'Error in network:{option}, Please try again ')
        return


def get_avg(apyL):
    total_added = 0.0
    ct = 0.0
    for line in apyL:
        total_added = total_added + float(line)
        ct += 1.0

    avg = total_added / ct

    apy_list = []
    count = 0.0
    while count != ct:
        count += 1
        apy_list.append(avg)

    return apy_list


def apyPlot(network):
    if network == option[0]:
        dates = list(optimismData['Date'])
        apyData = [line[:-1] for line in list(optimismData['APY'])]
        fig = go.Figure([go.Scatter(x=dates, y=apyData)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network == option[1]:
        dates = list(maticData['Date'])
        apyData = [line[:-1] for line in list(maticData['APY'])]
        fig = go.Figure([go.Scatter(x=dates, y=apyData)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network == option[2]:
        dates = list(binanceData['Date'])
        apyData = [line[:-1] for line in list(binanceData['APY'])]
        fig = go.Figure([go.Scatter(x=dates, y=apyData)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network == option[3]:
        dates = list(avalancheData['Date'])
        apyData = [line[:-1] for line in list(avalancheData['APY'])]
        fig = go.Figure([go.Scatter(x=dates, y=apyData)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return

    elif network != any(option):
        print(f'Error in network:{network}, Please try again!')


def avgApyPlot(network):
    if network == option[0]:
        mDates = list(optimismData['Date'])
        mAPYdata = [line[:-1] for line in list(optimismData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Optimism USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network == option[1]:
        mDates = list(maticData['Date'])
        mAPYdata = [line[:-1] for line in list(maticData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Matic USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network == option[2]:
        mDates = list(binanceData['Date'])
        mAPYdata = [line[:-1] for line in list(binanceData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Binance USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network == option[3]:
        mDates = list(avalancheData['Date'])
        mAPYdata = [line[:-1] for line in list(avalancheData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Avalanche USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return

    elif network != any(option):
        print(f'Error in network:{network}, Please try again!')
        return


def avgProfitPlot(deposit, network):
    deposit = float(deposit)

    if network == option[0]:

        data = estimate(deposit, option[0])
        dRange = [deposit - 100, data[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=oDates, y=oAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=oDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[1]:

        data = estimate(deposit, option[1])
        dRange = [deposit - 100, data[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[2]:

        data = estimate(deposit, option[2])
        dRange = [deposit - 100, data[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=bDates, y=bAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=bDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[3]:

        data = estimate(deposit, option[3])
        dRange = [deposit - 100, data[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=aDates, y=aAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=aDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Profit Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    else:
        print(f'Error in {network}: please try again')
        return


def profitWdeposit(initial, network, time_frame, amount):
    bw = 15
    m = 30
    c = 1

    profit = []

    if network == option[0]:

        for line in oPay:

            if time_frame == times[0]:
                # div_payment.append(initial * float(line))
                initial = initial * float(line) + initial + amount
                profit.append(initial)
            elif time_frame == times[1]:
                if c != bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1
            elif time_frame == times[2]:
                if c != m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1

        dRange = [profit[0] - 100, profit[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=oDates, y=oAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=oDates, y=profit, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Profit Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[1]:
        for line in mPay:

            if time_frame == times[0]:
                # div_payment.append(initial * float(line))
                initial = initial * float(line) + initial + amount
                profit.append(initial)
            elif time_frame == times[1]:
                if c != bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1
            elif time_frame == times[2]:
                if c != m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1

        dRange = [profit[0] - 100, profit[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=mDates, y=profit, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Profit Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[2]:

        for line in bPay:

            if time_frame == times[0]:
                # div_payment.append(initial * float(line))
                initial = initial * float(line) + initial + amount
                profit.append(initial)
            elif time_frame == times[1]:
                if c != bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1
            elif time_frame == times[2]:
                if c != m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1

        dRange = [profit[0] - 100, profit[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=bDates, y=bAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=bDates, y=profit, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Profit Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif network == option[3]:

        for line in aPay:

            if time_frame == times[0]:
                # div_payment.append(initial * float(line))
                initial = initial * float(line) + initial + amount
                profit.append(initial)
            elif time_frame == times[1]:
                if c != bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == bw:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1
            elif time_frame == times[2]:
                if c != m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial
                    profit.append(initial)
                    c += 1
                elif c == m:
                    # div_payment.append(initial * float(line))
                    initial = initial * float(line) + initial + amount
                    profit.append(initial)
                    c = 1

        dRange = [profit[0] - 100, profit[-1] + 100]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=aDates, y=aAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=aDates, y=profit, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=dRange, scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Profit Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()



profitWdeposit(1000, 'M', 'M', 50)
