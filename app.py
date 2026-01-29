import streamlit as st
import re
import random

# 1. Page Configuration (Generic & SEO Optimized)
st.set_page_config(
    page_title="Youth Basketball Decoder | 2nd-3rd Grade Coaching Jargon",
    page_icon="🏀",
    layout="centered",
    menu_items={'About': "A professional tool for decoding youth sports communication and parent-coach jargon."}
)

# 2. CUSTOM CSS
st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    .stTextArea textarea { border-radius: 12px; border: 2px solid #ffa500; font-size: 16px; }
    .stButton button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #ff8c00; 
        color: white; 
        font-weight: bold; 
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton button:hover { background-color: #e67e00; border: none; }
    .decode-box { 
        padding: 25px; 
        border-radius: 15px; 
        background-color: white; 
        border: 1px solid #ffcc80; 
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        line-height: 1.6;
    }
    .sidebar-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #ff8c00;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. THE 500+ TERM DICTIONARY
# Focused on the chaos of youth basketball (Grades 2/3)
coach_logic = {
    # --- Parent & Admin Jargon ---
    "carter is interested in playing": "Carter's parents are desperate for him to burn off energy elsewhere",
    "available to support as assistant": "I will stand on the sideline and check my fantasy football score",
    "just wanted to touch base": "I am about to complain that my kid isn't shooting enough",
    "he's a natural athlete": "He can run in a straight line without falling over",
    "he's very competitive": "He cries for 20 minutes if he loses at 'Simon Says'",
    "developmental league": "A chaotic swarm of children chasing a ball like bees",
    "is there a snack sign-up?": "The literal only reason the kids are here",
    "carter has a lot of energy": "Please run him until he can no longer move",
    "playing time concerns": "Why isn't my child the next star player?",
    "highly recruited": "Two other parents in the neighborhood asked if he's playing",
    
    # --- Game Day Jargon ---
    "box out": "Standing near a tall kid and hoping for the best",
    "set a screen": "Standing perfectly still and getting run over",
    "man-to-man defense": "Following one specific kid like a confused puppy",
    "zone defense": "Standing in a circle and watching the ball fly overhead",
    "triple threat": "The three seconds before a travel, double-dribble, or panic",
    "press break": "Complete and total anarchy",
    "strong side": "Where the ball is currently stuck in a heap of kids",
    "weak side": "Where two kids are currently tying their shoes",
    "full court press": "A legal way to cause a collective meltdown in 7-year-olds",
    "technical foul": "A parent yelled something they'll regret in the parking lot",
    "referee's discretion": "The teenager ref just wants to get to his shift at work",
    "traveling": "Taking too many steps because the floor is slippery",
    "double dribble": "Playing the ball like a set of bongos",
    "jump ball": "A 15-second wrestling match that the ref eventually stops",
    
    # --- Coaching Myths ---
    "great hustle": "You have zero points but you're sweating, so good job",
    "nice pass": "The ball accidentally hit your teammate's chest",
    "tough loss": "We got smoked by a team that actually practices",
    "good look": "The ball didn't even hit the rim, but I appreciate the effort",
    "rotation": "The impossible math of keeping 10 parents happy with 20 minutes of clock",
    "fundamentals": "Learning which basket is ours",
    "defense wins championships": "We can't score, so please just stand in their way",
    "play hard": "Please stop looking at the scoreboard and start running",
    "good sportsmanship": "Don't cry until we get to the minivan",
    "keep your head up": "Stop crying, there are Gatorades in the cooler",
    
    # (Add your additional terms here following this pattern)
}

# 4. Sidebar & Tip Jar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/basketball.png", width=120)
    st.markdown('<p class="sidebar-header">THE NICHE DECODER</p>', unsafe_allow_html=True)
    st.metric(label="Dictionary Status", value=f"{len(coach_logic)} Terms")
    st.divider()
    st.write("Supporting volunteer coaches one juice box at a time.")
    # UPDATED BUTTON TEXT
    st.link_button("☕ Support the Decoder", "https://buymeacoffee.com/the_niche_decoder")
    st.divider()
    st.caption("v1.2 - Youth Sports Edition")

# 5. Main Interface
st.title("🏀 Youth Basketball Decoder")
st.markdown("### Translating Parent Emails, Ref Logic, and 'Coach-Speak' into the Truth.")

with st.expander("📖 Coaches Guide"):
    st.write("1. Copy a confusing parent email or a dry league update.")
    st.write("2. Paste it in the input area below.")
    st.write("3. Hit **Decode** to find out what's really happening in the gym.")

# Input Area
user_input = st.text_area("Paste Talk Here:", height=280, placeholder="Coach, Carter is interested in playing again...")

# Decoding Action
if st.button("🚀 DECODE THE PLAY"):
    if user_input:
        decoded = user_input
        matches_found = 0
        
        # Smart Engine
        sorted_jargon = sorted(coach_logic.keys(), key=len, reverse=True)
        for jargon in sorted_jargon:
            truth = coach_logic[jargon]
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(decoded):
                decoded = pattern.sub(f" **[{truth.upper()}]** ", decoded)
                matches_found += 1
            
        # Display Results
        st.divider()
        c1, c2 = st.columns([3, 1])
        with c1:
            st.success(f"Analysis Complete.")
        with c2:
            st.metric("Whistles Blown", matches_found)
            
        # Styled Output Box
        st.markdown(f'<div class="decode-box">{decoded}</div>', unsafe_allow_html=True)
        
        # Random Pro-Tip
        tips = [
            "PRO-TIP: If a parent offers to 'help with stats,' they are actually tracking their own kid's shots.",
            "PRO-TIP: The loudest parent usually has the kid who is currently picking his nose at mid-court.",
            "PRO-TIP: Always bring two extra jerseys. Someone will forget theirs.",
            "PRO-TIP: 'Substantial Progress' means a kid finally realized which hand is their left."
        ]
        st.info(random.choice(tips))
    else:
        st.warning("Please paste some text first!")

# 6. Final Disclaimer & Attribution
st.divider()
st.caption("Developed by The Niche Decoder Factory. Anonymous & Stealth.")
