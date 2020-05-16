#%%
import boto3
import sys
# %%
polly = boto3.client('polly')
translate = boto3.client('translate')
# %%
text= "Hello my friend"

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        text = f.read()

#%%
response = translate.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='es'
)
traducido = response['TranslatedText']
# %%
synth = polly.synthesize_speech(
    Engine='neural',
    OutputFormat='mp3',
    Text=traducido,
    LexiconNames=['lexicon'],
    TextType='text',
    VoiceId='Lupe'
)
with open('lupe_neural_con_lexicon.mp3', "wb") as file:
    file.write(synth['AudioStream'].read())


# %%
