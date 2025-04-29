import streamlit as st
import openai

"""
    MusePal: An AI Tool Assistant for Musicians using streamlit AI agents
    Author:  Beck Sonstein
       Made for musicians who create beautiful songs through instruments,but struggle when it comes to transforming their melodies into rhythmic, creative lyrics.
       
    
       
    """

openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")
if not openai_api_key:
    st.warning("Please enter your OpenAI API key to generate your lyrics")
    st.stop()
else:
    openai.api_key = openai_api_key
          
            
            
 #################-Frontend-####################################           
st.markdown('<div class="title">MusePal: An AI Tool Assistant for Musicians</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="subtitle">
        Are you a passionate musician who creates beautiful songs through instruments, 
        but struggles when it comes to transforming their melodies into rhythmic, creative lyrics? 
        Let MusePal help you out.
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
 
    body {
        background: #1e1e2f;
        color: #f5f5f5;
        font-family: 'Helvetica';
    }

    
    .title {
        font-size: 3rem;
        font-weight: bold;
        color:rgb(37, 39, 99);
        text-align: center;
        margin-bottom: 20px;
    }


    .subtitle {
        font-size: 1.2rem;
        color:rgb(186, 204, 207);
        text-align: center;
        margin-bottom: 40px;
    }
 
    textarea, input {
        background-color: #2e2e3f;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 10px;
    }

    
    button {
        background-color: #ffcc00;
        color: #1e1e2f;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    button:hover {
        background-color: #e6b800;
    }

   
    .stWarning {
        background-color: #ffcc00;
        color: #1e1e2f;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }
 
    .generated-lyrics {
        background-color: #2e2e3f;
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 20px;
        margin-top: 20px;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inputs for song details
song_description = st.text_area("Song Description", "Describe the meaning and tone of your song...do you have any artists or songs in mind that you want to emulate?")
melody_details = st.text_input("Melody Details (Optional)", "Enter keywords or themes from your melody...give as much detail as you want!")

if st.button("Generate Lyrics"):
    with st.spinner("Brainstorming lyrics..."):
        user_prompt = (
            f"Meaning & Tone: {song_description}\n"
            f"Melody Details: {melody_details}\n\n"
            "Using these details, generate a complete set of song lyrics that are rhythmic, poetic, "
            f"{song_description}, with qualities: {melody_details}. "
            "Additionally create a fitting and artistic, poetic title for the song and put it at the top. "
            "The output should be structured into clearly labeled sections such as [Intro], [Verse 1], [Chorus], etc. "
            "The song should be coherent and consistent with its lyrics, matching the user's theme and/or story. "
            "And the song's structure should flow smoothly and consistently. For example, repetition should be used to create a catchy chorus, "
            "and the verses should build on the story or theme introduced in the intro. "
            "Within each section, each lyric sentence must appear on its own line. Do not include any extra commentary outside the lyric sections. "
            "Ensure the lyrics sound raw, human, creative and artistic, capturing vivid imagery and a rhythmic flow."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4", 
                messages=[
                    {
                        "role": "system",
                        "content": "You are a tortured, brilliant lyricist specializing in transforming ideas into rhythmic, catchy, poetic lyrics."
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                max_tokens=2500,
                temperature=0.9,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                n=1
            )

            lyrics = response.choices[0].message.content.strip()
            st.markdown('<div class="generated-lyrics">{}</div>'.format(lyrics.replace("\n", "<br>")), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred while generating lyrics: {e}")
            
  