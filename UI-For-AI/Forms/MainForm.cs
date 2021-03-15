// create by 刘晓林 and 高战立
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
using MySql.Data.MySqlClient;
using System.Diagnostics;
using System.Timers;

namespace AlphaBeatsUI
{
    public partial class MainForm : MetroForm
    {
        // 避免较短时间间隔中双击导致打开多个窗口
        private bool isClicked = false;

        public MainForm()
        {
            InitializeComponent();          
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            SlideForm slide = new SlideForm();
            slide.ShowDialog();
        }


        //给窗口加阴影
        private const int CS_DropShadow = 0x00020000;

        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams cp = base.CreateParams;
                cp.ClassStyle |= CS_DropShadow;
                return cp;
            }
        }

        //开始按钮
        private void StartButton_Click(object sender, EventArgs e)
        {

            string[] strArr = new string[2];
            string sArguments = null;

            // 设置定时器，3秒后调用函数
            System.Timers.Timer timer = new System.Timers.Timer();
            timer.Enabled = true;
            timer.Interval = 3000;//执行间隔时间,单位为毫秒
            timer.Start();
            timer.Elapsed += new System.Timers.ElapsedEventHandler(reSet);

            //当没有被连续点击时
            if (isClicked == false)
            {
                isClicked = true;

                // 根据选择打开相应的游戏
                switch (metroComboBox1.Text)
                {
                    case "Just Shapes and Beats":
                        // 利用process打开exe文件
                        string targetPath1 = string.Format(@"..\..\..\OpenAI\demo\dist\start\");
                        Process process1 = new Process();

                        process1.StartInfo.WorkingDirectory = targetPath1; // 初始化可执行文件的文件夹信息
                        process1.StartInfo.UseShellExecute = true;        // 使用操作系统shell启动进程
                        process1.StartInfo.FileName = "start.exe"; // 初始化可执行文件名
                        try
                        {
                            // 启动可执行文件
                            process1.Start();
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show(ex.Message.ToString());
                        }
                        break;

                    case "Flappy Huaji":
                        // 打开三个版本迭代的Flappy huaji版本
                        sArguments = @"..\..\..\FlappyBird\\Flappy--huaji0\index.html";
                        string path1 = @"..\..\..\FlappyBird\\Flappy--huaji1\index.html";
                        string path2 = @"..\..\..\FlappyBird\\Flappy--huaji2\index.html";
                        // 调用Process静态方法打开网页
                        Process.Start(sArguments);
                        Process.Start(path1);
                        Process.Start(path2);
                        break;

                    case "Space War":
                        string targetPath = string.Format(@"..\..\..\SpaceWar\");
                        Process process = new Process();

                        process.StartInfo.WorkingDirectory = targetPath; // 初始化可执行文件的文件夹信息
                        process.StartInfo.UseShellExecute = true;        // 使用操作系统shell启动进程
                        process.StartInfo.FileName = "ai_feiji.exe"; // 初始化可执行文件名
                        try
                        {
                            // 启动可执行文件
                            process.Start();
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show(ex.Message.ToString());
                        }
                        break;

                    case "Dinosaur":
                        string targetPath2 = string.Format(@"..\..\..\Dinosaur\test_model\");
                        Process process2 = new Process();

                        process2.StartInfo.WorkingDirectory = targetPath2; // 初始化可执行文件的文件夹信息
                        process2.StartInfo.UseShellExecute = true;        // 使用操作系统shell启动进程
                        process2.StartInfo.FileName = "test_model.exe"; // 初始化可执行文件名
                        try
                        {
                            // 启动可执行文件
                            process2.Start();
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show(ex.Message.ToString());
                        }
                        break;

                    case "Auto Drive":
                        // 打开Auto Drive程序
                        sArguments = @"..\..\..\Car\Pong.exe";
                        Process.Start(sArguments);
                        break;
                }
            }
            
            //string sArgum   ents = @"start.py"; //调用的python的文件名字
            //strArr[0] = "2";
            //strArr[1] = "3";
            //RunPythonScript(sArguments, "-u", strArr);
        }

        //重置isClicked
        private void reSet(object source, ElapsedEventArgs e)
        {
            isClicked = false;
        }

        //选取游戏
        private void FileInput_Click(object sender, EventArgs e)
        {
            //this.openFileDialog1.Filter = "exe文件(*.exe)|*.exe";
            //if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            //{
            //    FileInput.Text = this.openFileDialog1.FileName;
            //}
        }


        //执行Python脚本
        public static void RunPythonScript(string sArgName, string args = "", params string[] teps)
        {
            Process p = new Process();
            //如果配了python.exe，直接写"python.exe",否则使用绝对路径
            p.StartInfo.FileName = @"python.exe";
            foreach (string sigstr in teps)
            {
                sArgName += " " + sigstr;//传递参数
            }

            p.StartInfo.Arguments = sArgName;

            p.StartInfo.UseShellExecute = false;

            p.StartInfo.RedirectStandardOutput = true;

            p.StartInfo.RedirectStandardInput = true;

            p.StartInfo.RedirectStandardError = true;

            p.StartInfo.CreateNoWindow = true;

            p.Start();
            p.BeginOutputReadLine();
            
            p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived);
            Console.ReadLine();
            p.WaitForExit();
        }

        //输出打印的信息
        static void p_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            if (!string.IsNullOrEmpty(e.Data))
            {
                AppendText(e.Data + Environment.NewLine);
            }
        }

        public delegate void AppendTextCallback(string text);
        public static void AppendText(string text)
        {
            //此处在控制台输出.py文件print的结果
            Console.WriteLine(text);     
        }

        // 显示gif动图
        private void MetroComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (metroComboBox1.SelectedItem.ToString())
            {
                case "Flappy Huaji":
                    pictureBox1.Image = Image.FromFile(@"..\..\Resources\Flappy bird.gif");
                    break;
                case "Just Shapes and Beats":
                    pictureBox1.Image = Image.FromFile(@"..\..\Resources\Just Shapes & Beats Demo.gif");
                    break;
                case "Space War":
                    pictureBox1.Image = Image.FromFile(@"..\..\Resources\Space war.gif");
                    break;
                case "Dinosaur":
                    pictureBox1.Image = Image.FromFile(@"..\..\Resources\dinosaur.gif");
                    break;
                case "Auto Drive":
                    pictureBox1.Image = Image.FromFile(@"..\..\Resources\car.gif");
                    break;

                default:
                    break;

            }
        }
    }
}