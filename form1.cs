using System;
using System.Speech.Recognition;
using System.Speech.Synthesis;
using System.Windows.Forms;

namespace arduinoVoice2{

    public partial class Form1 : Form
    {
        int retort = 1;
       

        bool justAskedAboutOn = false, justAskedAboutOff = false, justAskedAboutAllIDo = false, justSaidYes = false, justSaidNo = false, waiting = false;
        public Form1()
        {
            InitializeComponent();
        }
        SpeechSynthesizer speechSynthesizerObj;
        SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine();
        private void Form1_Load(object sender, EventArgs e)
        {
            SpeechRecognitionEngine sRecognize = new SpeechRecognitionEngine();
            Choices sList = new Choices();
            sList.Add(new string[] {  
                "light on",  
                "light off"  
            });
            speechSynthesizerObj = new SpeechSynthesizer();
            Grammar gr = new Grammar(new GrammarBuilder(sList));
            speechSynthesizerObj.SpeakAsync("How would you like the light?");
            try
            {
                sRecognize.RequestRecognizerUpdate();
                sRecognize.LoadGrammar(gr);
                sRecognize.SpeechRecognized += sRecognize_SpeechRecognized;
                sRecognize.SetInputToDefaultAudioDevice();
                sRecognize.RecognizeAsync(RecognizeMode.Multiple);
                sRecognize.Recognize();
                
            }
            catch
            {
                return;
            }
        }
        private void sRecognize_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            {
                
                    if (e.Result.Text == "light on" && justAskedAboutOn == false)
                    {
                        serialPort1.Open();
                        serialPort1.Write("a"); //send a to Arduino  
                        serialPort1.Close();
                        speechSynthesizerObj = new SpeechSynthesizer();
                       // if(retort != 3)
                            speechSynthesizerObj.SpeakAsync("How would you like the light?");
                        //else if(retort == 3)
                           // speechSynthesizerObj.SpeakAsync("is this all I do?  Just kidding.  How would you like the light?");
                        
                        ++retort;
                        justAskedAboutOff = false;
                        justAskedAboutOn = true;
                    }
                    else if (e.Result.Text == "light off" && justAskedAboutOff == false)
                    {
                        serialPort1.Open();
                        serialPort1.Write("b"); //send b to Arduino  
                        serialPort1.Close();
                        speechSynthesizerObj = new SpeechSynthesizer();
                        speechSynthesizerObj.SpeakAsync("How would you like the light?");
                        ++retort;
                        justAskedAboutOn = false;
                        justAskedAboutOff = true;
                    }
                
                
                
            }
        }
    }
}
