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
      <body className="">
        <header>
          <Navbar />
        </header>
        <main className="flex justify-center min-h-screen bg-gray-100">
          {children}
        </main>
        <footer></footer>
      </body>
    </html>
  );
}
