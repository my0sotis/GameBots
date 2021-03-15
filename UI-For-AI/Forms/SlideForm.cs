using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MetroFramework.Forms;

namespace AlphaBeatsUI
{
    public partial class SlideForm : Form
    {
        public SlideForm()
        {
            InitializeComponent();
        }

        private void TimerClose_Tick(object sender, EventArgs e) //控制slideform自动关闭
        {
            //MainForm form = new MainForm();
            //form.Show();
            //this.Hide();
            //timerClose.Stop();
            this.Close();
            timerClose.Stop();
        }

        private void SlideForm_Load(object sender, EventArgs e)
        {
            timerClose.Start();
        }
    }
}
