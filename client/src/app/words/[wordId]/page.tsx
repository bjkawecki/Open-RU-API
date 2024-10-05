"use client";
import Link from "next/link";

export default function WordDetails({
  params,
}: {
  params: { wordId: string };
}) {
  return (
    <div className="flex flex-col space-y-5 items-start m-10">
      <h1 className="text-2xl">Details of word {params.wordId}</h1>
      <Link href={`/`} className="bg-yellow-400 px-3 py-2 rounded">
        Zurück
      </Link>
    </div>
  );
}
