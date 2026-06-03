import streamlit as st
from model import Subscription, TravelPlan, ModelConfig
from planner import piafica

if "subscription" not in st.session_state:
    st.session_state.subscription = [
        Subscription("biglietto", 11.20, 1),
        Subscription("settimanale", 32.20, 7),
        Subscription("mensile", 113.50, 30),
        Subscription("trimestrale", 308.00, 90),
    ]

if "days" not in st.session_state:
    st.session_state.days = [False] * 90

st.title("Ottimizzatore abbonamenti")

st.sidebar.header("⚙️ Abbonamenti")

subs = st.session_state.subscriptions

for i, sub in enumerate(subs):
    with st.sidebar.expander(f"{sub.name}"):

        name = st.text_input("Nome", sub.name, key=f"name{i}")
        cost = st.number_input("Costo", value=sub.cost, key=f"cost{i}")
        duration = st.number_input("Durata (giorni)", value=sub.duration, key=f"dur{i}")

        if st.button("Aggiorna", key=f"upd{i}"):
            subs[i] = Subscription(name, cost, duration)
            st.rerun()

        if st.button("Rimuovi", key=f"del{i}"):
            subs.pop(i)
            st.rerun()


st.sidebar.divider()

st.sidebar.subheader("+ Nuovo abbonamento")

new_name = st.sidebar.text_input("Nome nuovo")
new_cost = st.sidebar.number_input("Costo nuovo", value=0.0)
new_duration = st.sidebar.number_input("Durata nuova", value=1)

if st.sidebar.button("Aggiungi"):
    subs.append(Subscription(new_name, new_cost, new_duration))
    st.rerun()


st.subheader("Giorni di viaggio")

cols = st.columns(7)

for i in range(90):
    col = cols[i % 7]

    checked = col.checkbox(
        str(i + 1),
        value=st.session_state.days[i],
        key=f"day{i}"
    )

    st.session_state.days[i] = checked


if st.button("Calcola ottimo piano"):

    plan = TravelPlan(st.session_state.days)
    config = ModelConfig(st.session_state.subscriptions)

    result = pianifica(plan, config)

    st.subheader("Risultato")

    st.write(f"**Costo minimo:** {round(result['costo_minimo'], 2)} €")

    st.subheader("Abbonamenti consigliati")

    for start, end, name in result["abbonamenti"]:
        st.write(f"- **{name}**: giorni {start + 1} → {end + 1}")