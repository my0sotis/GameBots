namespace AlphaBeatsUI
{
    partial class SlideForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.slide = new AlphaBeatsUI.Slide();
            this.timerClose = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // slide
            // 
            this.slide.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.slide.Location = new System.Drawing.Point(0, -253);
            this.slide.Name = "slide";
            this.slide.Size = new System.Drawing.Size(640, 506);
            this.slide.TabIndex = 0;
            // 
            // timerClose
            // 
            this.timerClose.Enabled = true;
            this.timerClose.Interval = 4000;
            this.timerClose.Tick += new System.EventHandler(this.TimerClose_Tick);
            // 
            // SlideForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(640, 253);
            this.Controls.Add(this.slide);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "SlideForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "SlideForm";
            this.Load += new System.EventHandler(this.SlideForm_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private Slide slide;
        private System.Windows.Forms.Timer timerClose;
    }
}