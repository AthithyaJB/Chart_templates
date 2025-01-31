import plotly.graph_objects as go

# Define nodes (categories in the financial statement)
labels = [
    "Revenue", "Server", "Microsoft 365 Commercial", "Gaming", "LinkedIn", "Windows & Devices", "Search", "Other",
    "Gross Profit", "Cost of Revenue", "Operating Profit", "Operating Expenses", 
    "R&D", "S&M", "G&A", "Tax", "Other Expenses", "Net Profit"
]

# Define flows (from source to destination)
sources = [0, 0, 0, 0, 0, 0, 0, 0,  # Revenue -> Different Segments
           1, 2, 3, 4, 5, 6, 7,      # Each segment -> Revenue
           8, 8,                      # Gross Profit -> Cost of Revenue & Operating Profit
           10, 10, 10, 10, 10,        # Operating Profit -> Various expenses
           11, 11, 11, 11,            # Operating Expenses -> R&D, S&M, G&A
           15, 16                     # Tax & Other -> Net Profit
]

targets = [8, 8, 8, 8, 8, 8, 8, 8,  # Revenue -> Gross Profit
           0, 0, 0, 0, 0, 0, 0,      # Each segment -> Revenue
           9, 10,                    # Cost of Revenue, Operating Profit
           11, 15, 16, 17, 18,       # Operating Profit -> Expenses, Tax, Other, Net Profit
           12, 13, 14,               # Operating Expenses -> Breakdown
           18, 18                    # Tax & Other -> Net Profit
]

# Values (monetary flow)
values = [
    23.6, 21.1, 6.6, 4.6, 4.5, 3.5, 5.6, 6.8,  # Revenue breakdown
    23.6, 21.1, 6.6, 4.6, 4.5, 3.5, 5.6,       # Revenue -> Gross Profit
    21.8, 47.8,                                # Cost of Revenue, Gross Profit
    16.2, 5.3, 2.2, 7.9, 6.4,                  # Operating Profit -> Expenses
    7.9, 6.4, 1.8,                             # Operating Expenses Breakdown
    5.3, 2.2                                   # Tax, Other -> Net Profit
]

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
))

fig.update_layout(title_text="Microsoft Q2 FY25 Income Statement", font_size=12)
fig.show()