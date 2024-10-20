"use client";
import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex justify-center m-10">
      <div className="flex flex-col justify-center space-y-5 font-bold text-center min-w-1/4">
        <p className="text-3xl text-gray-700">Seite nicht gefunden (404)</p>
        <Link href={"/"} className="text-lg text-blue-500 underline">
          Zur Startseite
        </Link>
      </div>
    </div>
  );
}
