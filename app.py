import streamlit as st
import random 
choices={
    "rock":"rock.png",
    "paper":"paper.png",
    "scissor":"scissors.png"
}
users_choice=st.selectbox("Choose your option",choices.keys())
com=random.choice(list(choices.keys()))
if st.button("Play"):
    col1,col2,col3=st.columns([1,1,1])
    with col1:
        st.image(choices[users_choice])
    with col2:
        st.write("V/S")
    with col3:
        st.image(choices[com])


if (users_choice == "rock" and com == "scissor"):
    st.markdown("### You Win!")
elif (users_choice == "paper" and com == "rock"):
    st.markdown("### You Win!")
elif (users_choice == "scissor" and com == "paper"):
    st.markdown("### You Win!")
elif users_choice==com:
    st.markdown("### It's a tie!")
elif (users_choice == "scissor" and com == "rock"):
    st.markdown("### You lose!")
elif (users_choice == "rock" and com == "paper"):
    st.markdown("### You lose!")
elif (users_choice == "paper" and com == "scissor"):
    st.markdown("### You lose!")
    