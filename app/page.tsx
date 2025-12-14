"use client";

import { useState } from "react";
import Image from "next/image";

export default function Home() {
  const [files, setFiles] = useState<File[]>([]);

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        
        <Image
          className="dark:invert"
          src="/next.svg"
          alt="Next.js logo"
          width={100}
          height={20}
          priority
        />

        <div className="flex flex-col items-center gap-6 text-center sm:items-start sm:text-left">
          <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
            Upload files to get started
          </h1>

          {/* ✅ File input */}
          <input
            type="file"
            multiple
            onChange={(e) => setFiles(Array.from(e.target.files || []))}
            className="block w-full text-sm text-zinc-600
              file:mr-4 file:rounded-full file:border-0
              file:bg-black file:px-4 file:py-2
              file:text-white hover:file:bg-zinc-800
              dark:file:bg-white dark:file:text-black"
          />

          {/* Optional: show selected files */}
          {files.length > 0 && (
            <ul className="mt-4 text-sm text-zinc-600 dark:text-zinc-400">
              {files.map((file, idx) => (
                <li key={idx}>{file.name}</li>
              ))}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}
