import Link from "next/link";
import { WordClass } from "../app/enums";
import { Translation, Word } from "../app/types";

export function Table({ words }: any) {
  return (
    <div className="flex justify-center w-screen text-left">
      <div className="flex-row w-1/2 shadow">
        <div className="flex justify-around p-5 font-medium text-white uppercase bg-blue-500 border-b">
          <div>Russisch</div>
          <div>Wortart</div>
          <div>Deutsch</div>
        </div>
        {words.map((word: Word) => (
          <Link
            href={`/words/${word.id}`}
            key={word.id}
            className="flex text-center p-5 text-gray-700 bg-gray-50 border-b hover:bg-blue-100"
          >
            <div className="basis-1/3">{word.name_accent}</div>
            <div className="basis-1/3">{WordClass[word.word_class]}</div>
            <div className="basis-1/3">
              {word.translations.map(
                (translation: Translation, index: number) =>
                  (index ? ", " : "") + translation.name
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
