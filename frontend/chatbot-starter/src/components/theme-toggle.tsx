"use client"

import { useEffect, useState } from "react"
import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"
import { Sun, Moon } from "lucide-react"

interface ThemeToggleProps {
  onLightModeSwitch: () => void
}

export function ThemeToggle({ onLightModeSwitch }: ThemeToggleProps) {
  const { theme, setTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  const toggleTheme = () => {
    if (theme === "dark") {
      onLightModeSwitch()
    } else {
      setTheme("dark")
    }
  }

  if (!mounted) {
    return null
  }

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={toggleTheme}
      className="relative w-10 h-10 rounded-full bg-yellow dark:bg-turquoise"
    >
      {theme === "dark" ? (
        <Sun className="h-[1.2rem] w-[1.2rem] text-white" />
      ) : (
        <Moon className="h-[1.2rem] w-[1.2rem] text-yellow-dark" />
      )}
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}

