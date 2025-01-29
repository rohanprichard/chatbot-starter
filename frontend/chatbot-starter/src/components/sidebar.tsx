"use client"

import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Skeleton } from "@/components/ui/skeleton"
import { cn } from "@/lib/utils"
import { PlusCircle } from "lucide-react"
import { Sheet, SheetContent } from "@/components/ui/sheet"

interface SidebarProps {
  sessions: { id: string; name: string }[]
  activeSession: string | null
  onNewSession: () => void
  onSessionSelect: (id: string) => void
  isOpen: boolean
  onClose: () => void
  isLoading: boolean
}

export function Sidebar({
  sessions,
  activeSession,
  onNewSession,
  onSessionSelect,
  isOpen,
  onClose,
  isLoading,
}: SidebarProps) {
  const SidebarContent = (
    <div className="p-4 h-full flex flex-col">
      <Button
        variant="outline"
        className="w-full mb-4 bg-yellow dark:bg-turquoise hover:bg-yellow-dark dark:hover:bg-turquoise-dark transition-all duration-300 transform hover:scale-105 rounded-2xl"
        onClick={onNewSession}
        disabled={isLoading}
      >
        <PlusCircle className="mr-2 h-4 w-4 animate-pulse" />
        New Chat
      </Button>
      <ScrollArea className="flex-grow">
        {isLoading
          ? // Loading skeletons for sessions
            Array.from({ length: 5 }).map((_, index) => (
              <Skeleton key={`session-skeleton-${index}`} className="w-full h-10 mb-2 rounded-xl" />
            ))
          : sessions.map((session) => (
              <Button
                key={session.id}
                variant="ghost"
                className={cn(
                  "w-full justify-start mb-2 transition-all duration-300 transform hover:scale-105 rounded-xl",
                  activeSession === session.id
                    ? "bg-yellow dark:bg-turquoise hover:bg-yellow-dark dark:hover:bg-turquoise-dark"
                    : "hover:bg-yellow-light darkhover:bg-yellow-light dark:hover:bg-turquoise-light",
                )}
                onClick={() => onSessionSelect(session.id)}
              >
                {session.name}
              </Button>
            ))}
      </ScrollArea>
    </div>
  )

  return (
    <>
      {/* Mobile Sidebar */}
      <Sheet open={isOpen} onOpenChange={onClose}>
        <SheetContent side="left" className="w-[300px] sm:w-[400px]">
          {SidebarContent}
        </SheetContent>
      </Sheet>

      {/* Desktop Sidebar */}
      <div className="hidden md:block w-64 bg-white dark:bg-black bg-opacity-90 dark:bg-opacity-100 backdrop-blur-lg border-r border-white/20">
        {SidebarContent}
      </div>
    </>
  )
}

