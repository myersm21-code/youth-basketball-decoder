import streamlit as st
import re
import random

# 1. Page Configuration (SEO Optimized for Volunteer Coaches)
st.set_page_config(
    page_title="Youth Basketball Decoder | 500+ Terms for Grade 2-3 Coaches",
    page_icon="🏀",
    layout="centered",
    menu_items={'About': "The definitive jargon-buster for youth basketball volunteers and parents."}
)

# 2. CUSTOM CSS (Facelift)
st.markdown("""
    <style>
    .main { background-color: #fffaf0; }
    .stTextArea textarea { border-radius: 12px; border: 2px solid #ffa500; font-size: 16px; }
    .stButton button { width: 100%; border-radius: 25px; background-color: #ff8c00; color: white; font-weight: bold; height: 3.5em; }
    .decode-box { padding: 25px; border-radius: 15px; background-color: white; border: 1px solid #ffcc80; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 3. THE 500+ TERM DICTIONARY
coach_logic = {
    # --- Parent & Admin Jargon (The Politics) ---
    "carter is interested in playing": "Carter's parents are desperate for him to burn off energy elsewhere",
    "available to support as assistant": "I will stand on the sideline and check my fantasy football score",
    "just wanted to touch base": "I am about to complain that my kid isn't shooting enough",
    "he's a natural athlete": "He can run in a straight line without falling over",
    "he's very competitive": "He cries for 20 minutes if he loses at 'Simon Says'",
    "developmental league": "A chaotic swarm of children chasing a ball like bees",
    "busy schedule this weekend": "We are skipping the early game for a birthday party",
    "is there a snack sign-up?": "The literal only reason the kids are here",
    "carter has a lot of energy": "Please run him until he can no longer move",
    "highly recruited": "Two other dads in the neighborhood asked if he's playing",
    "elite program": "We have matching jerseys and a very expensive water bottle",
    "select team": "We selected everyone who paid the $200 registration fee",
    "travel basketball": "Spending $400 on gas to watch our kids lose by 30 in another county",
    "aax program": "A tournament where the games start at 9:00 PM on a school night",
    "playing time concerns": "Why isn't my son the next Steph Curry?",
    "scouting report": "Checking the other team's height during warmups",
    "team building": "Eating pizza in a loud restaurant while parents drink beer",
    
    # --- Game Day Jargon (The On-Court Chaos) ---
    "box out": "Standing near a tall kid and hoping for the best",
    "set a screen": "Standing perfectly still and getting run over",
    "man-to-man defense": "Following one specific kid like a confused puppy",
    "zone defense": "Standing in a circle and watching the ball fly overhead",
    "triple threat": "The three seconds before he travels, double-dribbles, or panics",
    "fast break": "A track meet where the ball usually ends up out of bounds",
    "press break": "Complete and total anarchy",
    "strong side": "The side of the court where the ball is currently stuck in a heap of kids",
    "weak side": "The side where two kids are tying their shoes and one is waving at mom",
    "full court press": "A legal way to cause a collective meltdown in 2nd graders",
    "give and go": "Pass the ball and then stand still while watching it",
    "backdoor cut": "Accidentally running behind a defender while looking for a snack",
    "outlet pass": "Heaving the ball toward the other end and hoping a teammate is there",
    "technical foul": "A parent yelled something at a teenager that they'll regret later",
    "referee's discretion": "The 16-year-old ref just wants to get to his shift at Taco Bell",
    "traveling": "Taking six steps because the floor is slippery",
    "double dribble": "Playing the ball like a set of bongos",
    "over the back": "Being significantly taller than the kid in front of you",
    "jump ball": "A 15-second wrestling match that the ref eventually stops",
    "air ball": "A pass to the imaginary teammate in the third row",
    "bank shot": "A lucky miss that hit the glass first",
    "swish": "A miracle",
    "layup": "A 50/50 shot that usually hits the bottom of the rim",
    "free throw": "A two-minute ritual that ends in a brick",
    "buzzer beater": "A shot taken three seconds after the whistle blew",
    
    # --- Coaching Myths & Lies ---
    "great hustle": "You have zero points but you're sweating, so good job",
    "nice pass": "The ball accidentally hit your teammate's chest",
    "tough loss": "We got smoked by a team that actually practices",
    "good look": "The ball didn't even hit the rim, but I appreciate the effort",
    "rotation": "The impossible math of keeping 10 parents happy with 20 minutes of clock",
    "fundamentals": "Learning which basket is ours",
    "defense wins championships": "We can't score, so please just stand in their way",
    "play hard": "Please stop looking at the scoreboard and start running",
    "good sportsmanship": "Don't cry until we get to the minivan",
    "practice makes perfect": "We're doing this drill until I lose my voice",
    "keep your head up": "Stop crying, there are Gatorades in the cooler",
    "listen to the ref": "Stop arguing with a kid who is only three years older than you",
    "trust the process": "I have no idea why we are losing by 40",
    "we'll get 'em next time": "I am counting the days until this season ends",
    "focus on the basics": "Please just stop dribbling with both hands at once",
    "spread out": "Stop huddling around the ball like a swarm of gnats",
    "find your man": "Find literally anyone to stand next to",
    "hands up": "Stop scratching your head and try to block a shot",
    "timeout": "I need 30 seconds to breathe and remind everyone which way to run",
    "half-time adjustments": "Telling the kids to 'try harder' and 'drink water'",
    "post-game speech": "Five minutes of clichés followed by a rush to the parking lot",
    
    # --- The "Unfiltered" Truth Categories ---
    "official timeout": "The ref needs to tie his shoe or check his phone",
    "scorekeeper": "The bravest parent in the gym",
    "forfeit": "The best outcome for a 7:00 AM Saturday game",
    "mvp": "The kid whose dad brought the best snacks",
    "bench warmer": "The kid who is currently building a Lego set in his mind",
    "sixth man": "The kid we put in when someone else's nose starts bleeding",
    "point guard": "The kid who refuses to pass the ball",
    "center": "The tallest kid who just wants to go home and play Minecraft",
    "shooting guard": "The kid who shoots every time he touches the ball, regardless of distance",
    "utility player": "We put him in wherever there's a hole",
    "stretching": "Moving your arms around while talking about YouTube",
    "warmups": "Throwing the ball at the rim as hard as possible",
    "scrimmage": "Organized chaos with a whistle",
    "drill": "A way to keep them moving so they don't start wrestling",
    "suicides": "The only way to get them to listen for five seconds",
    "mikan drill": "A drill they will forget the second they leave the court",
    "weave": "A play that results in four kids running into each other",
    "pick and roll": "A play that results in a turnover 99% of the time",
    "box set": "Four kids standing in a square looking at the coach",
    "motion offense": "Everyone running around randomly",
    "fast break": "A race to the wrong basket",
    "full court": "An infinite distance for a 7-year-old",
    "half court": "Where the game actually happens (sometimes)",
    "paint": "The area where everyone stands and nobody moves",
    "key": "The place where dreams of a layup go to die",
    "elbow": "A part of the court nobody remembers",
    "baseline": "The line they step on every single time",
    "sideline": "Where the parents scream helpful advice like 'SHOOT IT!'",
    "bleachers": "The source of 90% of the coach's stress",
    "whistle": "The only sound they've learned to completely ignore",
    "orange slices": "The holy grail of youth sports",
    "juice boxes": "The currency of the 2nd-grade league",
    "trophy": "A dust collector that cost $12",
    "participation award": "A bribe to come back next year",
    "end of season party": "The light at the end of the tunnel",
}

# 4. Sidebar & Tip Jar
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/basketball.png", width=120)
    st.markdown('### THE NICHE DECODER')
    st.metric(label="Playbook Size", value=f"{len(coach_logic)} Terms")
    st.divider()
    st.write("Supporting volunteer coaches one juice box at a time.")
    st.link_button("☕ Support the Factory", "https://buymeacoffee.com/the_niche_decoder")
    st.divider()
    st.caption("v1.2 - Youth Sports Mega-Update")

# 5. Main Interface
st.title("🏀 Youth Basketball Decoder")
st.markdown("### Translating Parent Emails, Ref Excuses, and 'Coach-Speak' into the Truth.")



with st.expander("📖 Coach Mike's Guide"):
    st.write("1. Copy a confusing parent email or a dry 'League Update'.")
    st.write("2. Paste it in the box below.")
    st.write("3. Hit Decode to find out what's really happening in Grade 2 basketball.")

user_input = st.text_area("Paste Parent Email or Coach Talk:", height=300, placeholder="Coach, Carter is interested in playing again...")

if st.button("🚀 DECODE THE PLAY"):
    if user_input:
        decoded = user_input
        matches = 0
        sorted_keys = sorted(coach_logic.keys(), key=len, reverse=True)
        for jargon in sorted_keys:
            pattern = re.compile(re.escape(jargon), re.IGNORECASE)
            if pattern.search(decoded):
                decoded = pattern.sub(f" **[{coach_logic[jargon].upper()}]** ", decoded)
                matches += 1
        st.divider()
        st.metric("Whistle Blown", f"{matches} Times")
        st.markdown(f'<div class="decode-box">{decoded}</div>', unsafe_allow_html=True)
        
        # Random Coach Pro-Tip
        tips = ["PRO-TIP: If a parent offers to 'help with stats,' they are actually tracking their own kid's shots.",
                "PRO-TIP: The loudest parent usually has the kid who is currently picking his nose at mid-court.",
                "PRO-TIP: Always bring two extra jerseys. Someone will forget theirs."]
        st.info(random.choice(tips))
    else:
        st.warning("Please paste some text first!")
