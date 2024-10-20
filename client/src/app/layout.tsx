import type { Metadata } from "next";
import { Navbar } from "../components/navbar";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Start | Wörterbuch",
    template: "%s | Wörterbuch",
  },
  description: "Russisch Wörter in Hülle und Fülle",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning={true}>
      <body className="bg-gray-200">
        <header>
          <Navbar />
        </header>
        <main>{children}</main>
        <footer></footer>
      </body>
    </html>
  );
}
