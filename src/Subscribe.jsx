import { Amplify } from "aws-amplify";
import { generateClient } from "aws-amplify/api";
import { useEffect, useState } from "react";
import { sendMessage } from "./graphql/mutations";
import { onMessage } from "./graphql/subscriptions";

const client = generateClient();

export default function Subscribe() {
  const [data, setData] = useState("");
  const [received, setReceived] = useState("");
  const [received2, setReceived2] = useState("");
  const [tenantCode, setTenantCode] = useState("4653");
  const [id, setId] = useState("");

  // Publish data to subscribed clients
  async function handleSubmit(evt) {
    evt.preventDefault();
    if (!data) return;
    await client.graphql({
      query: sendMessage,
      variables: { data },
    });
  }

  // subscribe to events
  useEffect(() => {
    console.log("tenantCode", tenantCode);
    console.log("before suscribe", client.subscriptions);
    const sub = client
      .graphql({ query: onMessage, variables: { tenantCode } })
      .subscribe({
        next: ({ data }) => {
          console.log("@@@@", data.onMessage);
          setReceived(JSON.stringify(data.onMessage));
        },
        error: (error) => console.warn(error),
      });
    console.log("after suscribe", client.subscriptions);

    return () => sub.unsubscribe();
  }, [tenantCode]);

  // subscribe to events
  useEffect(() => {
    console.log("id", id);
    const sub = client
      .graphql({ query: onMessage, variables: { tenantCode, id } })
      .subscribe({
        next: ({ data }) => {
          console.log("@@@@", data.onMessage);
          setReceived2(JSON.stringify(data.onMessage));
        },
        error: (error) => console.warn(error),
      });
    return () => sub.unsubscribe();
  }, [id]);

  return (
    <div className="App">
      CCI: <input onChange={(e) => setTenantCode(e.target.value)} />
      ID: <input onChange={(e) => setId(e.target.value)} />
      <header className="App-header">
        <p>Send/Push JSON to channel &quot;{name}&quot;...</p>
        <form onSubmit={handleSubmit}>
          <textarea
            rows="5"
            cols="60"
            name="description"
            onChange={(e) => setData(e.target.value)}
            value={data}
            placeholder="Enter valid JSON here... (use quotes for keys and values)"
          ></textarea>
          <br />
          <input type="submit" value="Submit" />
        </form>
        <p>Subscribed/Listening to channel &quot;{name}&quot;...</p>
        received
        <pre>{!received || JSON.stringify(JSON.parse(received), null, 2)}</pre>
        received2
        <pre>
          {!received2 || JSON.stringify(JSON.parse(received2), null, 2)}
        </pre>
      </header>
    </div>
  );
}
