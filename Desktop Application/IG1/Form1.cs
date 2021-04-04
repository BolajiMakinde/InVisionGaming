using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;

namespace IG1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.BackColor = Color.Wheat;
            this.TransparencyKey = Color.Wheat;

      
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int width = this.Size.Width;
            int height = this.Size.Height;
            int top = this.Top;
            int left = this.Left;

            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/screenCoordinates.txt")) {
                writer.WriteLine(width.ToString());
                writer.WriteLine(height.ToString());
                writer.WriteLine(top.ToString());
                writer.WriteLine(left.ToString());
            }
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            int width = this.Size.Width;
            int height = this.Size.Height;
            int top = this.Top;
            int left = this.Left;

            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/screenCoordinates.txt"))
            {
                writer.WriteLine(width.ToString());
                writer.WriteLine(height.ToString());
                writer.WriteLine(top.ToString());
                writer.WriteLine(left.ToString());
            }
        }
        private void numericUpDown6_ValueChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/offsets.txt"))
            {
                //top
                writer.WriteLine(this.numericUpDown6.Value.ToString());
                //left
                writer.WriteLine(this.numericUpDown2.Value.ToString());
                //width
                writer.WriteLine(this.numericUpDown3.Value.ToString());
                //height
                writer.WriteLine(this.numericUpDown4.Value.ToString());
            }
        }
        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/offsets.txt"))
            {
                //top
                writer.WriteLine(this.numericUpDown6.Value.ToString());
                //left
                writer.WriteLine(this.numericUpDown2.Value.ToString());
                //width
                writer.WriteLine(this.numericUpDown3.Value.ToString());
                //height
                writer.WriteLine(this.numericUpDown4.Value.ToString());
            }
        }

        private void numericUpDown3_ValueChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/offsets.txt"))
            {
                //top
                writer.WriteLine(this.numericUpDown6.Value.ToString());
                //left
                writer.WriteLine(this.numericUpDown2.Value.ToString());
                //width
                writer.WriteLine(this.numericUpDown3.Value.ToString());
                //height
                writer.WriteLine(this.numericUpDown4.Value.ToString());
            }
        }

        private void numericUpDown4_ValueChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/offsets.txt"))
            {
                //top
                writer.WriteLine(this.numericUpDown6.Value.ToString());
                //left
                writer.WriteLine(this.numericUpDown2.Value.ToString());
                //width
                writer.WriteLine(this.numericUpDown3.Value.ToString());
                //height
                writer.WriteLine(this.numericUpDown4.Value.ToString());
            }
        }

        private void numericUpDown5_ValueChanged(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/readFrequency.txt"))
            {
                writer.WriteLine(this.numericUpDown5.Value.ToString());
            }
        }

        private void comboBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("C:/Users/hb22h/OneDrive/Documents/GitHub/InVisionGaming/HapticState/inputType.txt"))
            {
                writer.WriteLine(this.comboBox1.Text);
            }
        }
    }
}
