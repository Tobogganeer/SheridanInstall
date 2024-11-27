namespace SheridanInstall.Net
{
    partial class Form1
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
            this.SlateCheckbox = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // SlateCheckbox
            // 
            this.SlateCheckbox.AutoSize = true;
            this.SlateCheckbox.Location = new System.Drawing.Point(96, 64);
            this.SlateCheckbox.Name = "SlateCheckbox";
            this.SlateCheckbox.Size = new System.Drawing.Size(60, 17);
            this.SlateCheckbox.TabIndex = 0;
            this.SlateCheckbox.Text = "SLATE";
            this.SlateCheckbox.UseVisualStyleBackColor = true;
            this.SlateCheckbox.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.SlateCheckbox);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox SlateCheckbox;
    }
}

