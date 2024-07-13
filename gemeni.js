const { GoogleGenerativeAI } = require("@google/generative-ai");
const gTTS = require('gtts');
const player = require('play-sound')(opts = {})
console.log("running...")
GEMINI_API_KEY = "AIzaSyBY23p5DZBjw5xx_FTuOIVwB-1HS0HZ79Y"

// Access your API key as an environment variable (see "Set up your API key" above)
const genAI = new GoogleGenerativeAI(GEMINI_API_KEY);

async function run() {
  // The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});

  const prompt = "response in json tell me what is highest speed recorded in cars with full details"

  const result = await model.generateContent(prompt);
  const response = await result.response;
  const text = response.text();
  console.log(text)
//   
speaker(text)
}
const speaker = (speech)=>{
    const  gtts = new gTTS(speech, 'en');
    gtts.save('Voice.mp3', function (err, result){
        if(err) { throw new Error(err); }
        console.log("Text to speech playing!");
        player.play('Voice.mp3', function(err){
            if (err) throw err
          })
    });
}
run();
// speaker(run())
