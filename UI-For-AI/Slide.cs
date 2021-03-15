using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AlphaBeatsUI
{
    public partial class Slide : UserControl
    {
        public Slide()
        {
            InitializeComponent();
        }

        private void Slide_Load(object sender, EventArgs e)
        {
            panel1.Size = new Size(panel1.Width, 30);
        }
        int panel1_y = 30;
        int waiter = 0;
        private void TimerSlide_Tick(object sender, EventArgs e)
        {
            waiter++;
            if(waiter > 150)
            {
                panel1_y += 6;
                panel1.Size = new Size(panel1.Width, panel1_y);
                if(panel1_y > 253)
                {
                    panel2.Hide();
                    timerSlide.Enabled = false;
                }
            }

        }
    }
}
