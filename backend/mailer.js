import nodemailer from 'nodemailer';

export async function sendAlertEmail(subject, message) {
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.ALERT_EMAIL,        // exemple : bot@tondomaine.com
      pass: process.env.ALERT_EMAIL_PASS,   // mot de passe ou App Password
    },
  });

  const mailOptions = {
    from: process.env.ALERT_EMAIL,
    to: process.env.ADMIN_EMAIL, // toi
    subject: subject,
    text: message,
  };

  await transporter.sendMail(mailOptions);
}

