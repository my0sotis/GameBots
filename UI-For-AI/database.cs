// create by 高战立
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace AlphaBeatsUI
{
    class database
    {
        public static database dbcon = new database();  //声明静态实例，通过该示例获取数据库连接
        private MySqlConnection conn = null;                 //数据库连接对象

        private database()                                                //私有构造函数
        {
            createConnection();
        }

        private void createConnection()                         //连接mysql数据库
        {
            try
            {
                //
                //此处注意修改mysql数据库密码和对应数据库的名称即——database
                //
                string mysql_conn = "server=localhost;user id=root;password=159357258;database=world";
                conn = new MySqlConnection(mysql_conn);
                conn.Open();
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message.ToString());
            }
        }

        public MySqlConnection getConnection()
        {
            return conn;                                                    //返回连接
        }
    }
}
