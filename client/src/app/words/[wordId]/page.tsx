import type { Metadata } from "next";
import Link from "next/link";

export const generateMetadata = ({ params }: Props): Metadata => {
  return {
    title: `Word ${params.wordId}`,
  };
};

type Props = {
  params: {
    wordId: string;
  };
};

export default function WordDetails({ params }: Props) {
  return (
    <div className="flex flex-col items-start m-10 space-y-5">
      <h1 className="text-2xl">Details of word {params.wordId}</h1>
      <Link href={`/`} className="py-2 px-3 bg-yellow-400 rounded">
        Zurück
      </Link>
    </div>
  );
}
