import { getUserInfoTool } from "@/lib/tools/user-info";
import { openai } from "@ai-sdk/openai";
import { streamText } from "ai";

export async function POST(req: Request) {
  const { messages } = await req.json();

  // streamText is used to run the request
  const result = streamText({
    messages,
    model: openai("gpt-4o-mini"),
    // Provides external tools the model can call.
    // In this case, a User Info tool.
    tools: { getUserInfoTool },
    maxSteps: 2,
    onError({ error }) {
      console.error("streamText error", { error });
    },
  });

  return result.toDataStreamResponse();
}
import { NextRequest } from 'next/server';
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { googleCalendarViewTool } from '@/lib/tools/google-calendar-view';

export async function POST(req: NextRequest) {
  // Get user prompt from request.
  const { prompt }: { prompt: string } = await req.json();

  // Initiates a streaming AI response.
  const result = streamText({
    prompt,
    model: openai('gpt-4o-mini'),
    // Provides external tools the model can call.
    // In this case, Google Calendar integration.
    tools: { googleCalendarViewTool },
    maxSteps: 2,
    onError({ error }) {
      console.error('streamText error', { error });
    },
  });

  // Converts the streaming result into a Next.js-compatible response.
  return result.toDataStreamResponse();
}
import { createDataStreamResponse, Message, streamText } from "ai";
import { checkUsersCalendar } from "@/lib/tools/";
import { setAIContext } from "@auth0/ai-vercel";
import { errorSerializer, withInterruptions } from "@auth0/ai-vercel/interrupts";
import { openai } from "@ai-sdk/openai";

export async function POST(request: Request) {
  const { id, messages} = await request.json();
  const tools = { checkUsersCalendar };
  setAIContext({ threadID: id });

  return createDataStreamResponse({
    execute: withInterruptions(
      async (dataStream) => {
        const result = streamText({
          model: openai("gpt-4o-mini"),
          system: "You are a friendly assistant! Keep your responses concise and helpful.",
          messages,
          maxSteps: 5,
          tools,
        });

        result.mergeIntoDataStream(dataStream, {
          sendReasoning: true,
        });
      },
      { messages, tools }
    ),
    onError: errorSerializer((err) => {
      console.log(err);
      return "Oops, an error occured!";
    }),
  });
}
import { z } from 'zod';
import { streamText, tool } from "ai"
import { openai } from "@ai-sdk/openai"
const { Octokit } = require("@octokit/rest");

import { listRepos } from "@/lib/tools/listRepos";

export const maxDuration = 60;

export async function POST(req) {
  const { messages } = await req.json()

  const response = streamText({
    model: openai('gpt-4o'),
    messages,
    system: "You're a helpful AI agent that fetches GitHub repositories",
    tools: { listRepos }
  })
  return response.toDataStreamResponse();
}
import { createDataStreamResponse, Message, streamText } from "ai";
import { listChannels } from "@/lib/tools/";
import { setAIContext } from "@auth0/ai-vercel";
import { errorSerializer, withInterruptions } from "@auth0/ai-vercel/interrupts";
import { openai } from "@ai-sdk/openai";

export async function POST(request: Request) {
  const { id, messages} = await request.json();
  const tools = { listChannels };
  setAIContext({ threadID: id });

  return createDataStreamResponse({
    execute: withInterruptions(
      async (dataStream) => {
        const result = streamText({
          model: openai("gpt-4o-mini"),
          system: "You are a friendly assistant! Keep your responses concise and helpful.",
          messages,
          maxSteps: 5,
          tools,
        });

        result.mergeIntoDataStream(dataStream, {
          sendReasoning: true,
        });
      },
      { messages, tools }
    ),
    onError: errorSerializer((err) => {
      console.log(err);
      return "Oops, an error occured!";
    }),
  });
}