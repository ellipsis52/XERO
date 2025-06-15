import mongoose from 'mongoose';

const transactionSchema = new mongoose.Schema({
  paymentId: String,
  amount: Number,
  created: Date,
  gptAnalysis: {
    risque: String,
    raison: String,
    action: String,
  }
});

export default mongoose.model('Transaction', transactionSchema);
