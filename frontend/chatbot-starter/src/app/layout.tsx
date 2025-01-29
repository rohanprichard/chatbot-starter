import type { Metadata } from "next"
import { Playfair_Display, Lato } from "next/font/google"
import "./globals.css"
import { ThemeProvider } from "@/components/theme-provider"

const playfair = Playfair_Display({ subsets: ["latin"] })
const lato = Lato({ weight: ["400", "700"], subsets: ["latin"] })

export const metadata: Metadata = {
  title: "FunChat",
  description: "A fun and interactive chat application",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${lato.className} ${playfair.className}`}>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange>
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}

