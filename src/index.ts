import { setAIContext } from "@auth0/ai-vercel";
import crypto from "node:crypto";
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

import { buy } from "./lib/tools/buy";

async function main() {
  const threadID = crypto.randomUUID();
  setAIContext({ threadID });

  console.log(
    "Check your mobile device for Auth0 Guardian notification and approve the request"
  );

  const { text } = await generateText({
    model: openai("gpt-4o-mini"),
    prompt: "Buy 3 stocks of Google",
    maxSteps: 2,
    tools: {
      // pass an Auth0 user id. For example, 'genai-5232571930223058' or 'google-oauth2|100000000000000000000'
      buy: buy({ userId: "<authenticated-user-id>" }),
    },
  });

  console.log(text);
}

main().catch(console.error);
import "dotenv/config";

import { OpenAIEmbeddings } from "@langchain/openai";
import { MemoryVectorStore } from "langchain/vectorstores/memory";
import { FGARetriever } from "@auth0/ai-langchain";

import { readDocuments, RetrievalAgent } from "./helpers";

async function main() {
  console.info(
    "\n..:: LangGraph Agents Example: Agentic Retrieval with Auth0 FGA \n\n"
  );

  const user = "user1";
  // 1. Read and load documents from the assets folder
  const documents = await readDocuments();
  // 2. Create an in-memory vector store from the documents for OpenAI models.
  const vectorStore = await MemoryVectorStore.fromDocuments(
    documents,
    new OpenAIEmbeddings({ model: "text-embedding-3-small" })
  );
  // 3. Create a retriever that uses FGA to gate fetching documents on permissions.
  const retriever = FGARetriever.create({
    retriever: vectorStore.asRetriever(),
    // FGA tuple to query for the user's permissions
    buildQuery: (doc) => ({
      user: `user:${user}`,
      object: `doc:${doc.metadata.id}`,
      relation: "viewer",
    }),
  });
  // 4. Convert the retriever into a tool for an agent.
  const fgaTool = retriever.asJoinedStringTool();
  // 5. The agent will call the tool, rephrasing the original question and
  // populating the "query" argument, until it can answer the user's question.
  const retrievalAgent = RetrievalAgent.create([fgaTool]);
  // 6. Query the retrieval agent with a prompt
  const answer = await retrievalAgent.query("Show me forecast for ZEKO?");

  console.info(answer);
}

main().catch(console.error);