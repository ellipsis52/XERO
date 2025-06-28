import { Auth0AI } from "@auth0/ai-vercel";
import { auth0 } from "@/lib/auth0";

const auth0AI = new Auth0AI();

export const withSlack = auth0AI.withTokenForConnection({
  connection: "sign-in-with-slack",
  scopes: ["channels:read", "groups:read"],
  refreshToken: async () => {
    const session = await auth0.getSession();
    const refreshToken = session?.tokenSet.refreshToken as string;

    return refreshToken;
  },
});