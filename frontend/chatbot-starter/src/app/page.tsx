"use client"

import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import { Skeleton } from "@/components/ui/skeleton"
import { cn } from "@/lib/utils"
import { Send, Menu } from "lucide-react"
import { ThemeToggle } from "@/components/theme-toggle"
import { LightModeWarningModal } from "@/components/light-mode-warning-modal"
import { Sidebar } from "@/components/sidebar"
import { Overlay } from "@/components/overlay"
import { Playfair_Display } from "next/font/google"

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
})

interface ChatSession {
  id: string
  name: string
}

interface Message {
  role: "user" | "assistant"
  content: string
}

const mockSessions: ChatSession[] = [
  { id: "1", name: "AI in Healthcare" },
  { id: "2", name: "Future of Technology" },
  { id: "3", name: "Climate Change Solutions" },
]

const mockMessages: { [key: string]: Message[] } = {
  "1": [
    { role: "assistant", content: "Hello! Welcome to our discussion on AI in Healthcare. How can I assist you today?" },
    { role: "user", content: "Can you give me an overview of how AI is being used in healthcare?" },
    {
      role: "assistant",
      content:
        "AI is being used in various ways in healthcare:\n\n1. Diagnosis: AI algorithms can analyze medical images and patient data to assist in diagnosing diseases.\n\n2. Drug Discovery: AI accelerates the process of identifying potential new drugs.\n\n3. Personalized Treatment: AI helps in creating personalized treatment plans based on a patient's genetic makeup and medical history.\n\n4. Robotic Surgery: AI-powered robots assist surgeons in performing complex procedures with greater precision.\n\n5. Administrative Tasks: AI automates routine administrative work, freeing up healthcare professionals to focus more on patient care.\n\nWould you like me to elaborate on any of these areas?",
    },
  ],
  "2": [
    {
      role: "assistant",
      content: "Welcome to our discussion on the Future of Technology. What aspect would you like to explore?",
    },
    {
      role: "user",
      content: "I'm curious about the potential impact of quantum computing. Can you tell me more about that?",
    },
    {
      role: "assistant",
      content:
        "Quantum computing is an exciting field with enormous potential:\n\n1. Cryptography: Quantum computers could break many current encryption methods, necessitating new quantum-resistant cryptography.\n\n2. Drug Discovery: They could simulate complex molecular interactions, dramatically speeding up the development of new medicines.\n\n3. Financial Modeling: Quantum computing could revolutionize risk assessment and portfolio optimization in finance.\n\n4. Climate Modeling: It could enable more accurate climate simulations, aiding in our understanding and mitigation of climate change.\n\n5. Artificial Intelligence: Quantum machine learning algorithms could potentially outperform classical algorithms in certain tasks.\n\nDo you want to dive deeper into any of these applications?",
    },
  ],
  "3": [
    {
      role: "assistant",
      content: "Welcome to our discussion on Climate Change Solutions. What specific area would you like to focus on?",
    },
    {
      role: "user",
      content: "I'm interested in renewable energy technologies. What are some promising developments in this field?",
    },
    {
      role: "assistant",
      content:
        "Great question! There are several exciting developments in renewable energy:\n\n1. Solar Power: Perovskite solar cells are showing promise for higher efficiency and lower costs than traditional silicon cells.\n\n2. Wind Energy: Floating offshore wind turbines are opening up new possibilities for wind farms in deeper waters.\n\n3. Energy Storage: Solid-state batteries and flow batteries are advancing, potentially providing more efficient and safer energy storage solutions.\n\n4. Hydrogen Fuel: Green hydrogen production through electrolysis powered by renewable energy is gaining traction as a clean fuel source.\n\n5. Tidal and Wave Energy: New designs for harnessing ocean energy are becoming more efficient and resilient.\n\nWould you like more details on any of these technologies?",
    },
  ],
}

const PlatypusIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 512 512"
    className="h-8 w-8 mr-2"
    fill="currentColor"
  >
    <path d="M432 256c0 17.7-14.3 32-32 32H336c-17.7 0-32-14.3-32-32s14.3-32 32-32h64c17.7 0 32 14.3 32 32zm-336-32h64c17.7 0 32 14.3 32 32s-14.3 32-32 32H96c-17.7 0-32-14.3-32-32s14.3-32 32-32zm336-96H96C43 128 0 171 0 224v64c0 53 43 96 96 96h320c53 0 96-43 96-96v-64c0-53-43-96-96-96zm-64 160c0 8.8-7.2 16-16 16H176c-8.8 0-16-7.2-16-16v-32c0-8.8 7.2-16 16-16h176c8.8 0 16 7.2 16 16v32z"/>
    <circle cx="144" cy="288" r="32"/>
    <circle cx="368" cy="288" r="32"/>
  </svg>
)

export default function ChatPage() {
  const [sessions, setSessions] = useState<ChatSession[]>([])
  const [activeSession, setActiveSession] = useState<string | null>(null)
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const { theme, setTheme } = useTheme()
  const [isWarningModalOpen, setIsWarningModalOpen] = useState(false)
  const [hasShownWarning, setHasShownWarning] = useState(false)
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)
  const [isLoadingSessions, setIsLoadingSessions] = useState(true)
  const [isLoadingMessages, setIsLoadingMessages] = useState(false)

  useEffect(() => {
    // Simulate fetching sessions
    setTimeout(() => {
      setSessions(mockSessions)
      setIsLoadingSessions(false)
    }, 1500)
  }, [])

  useEffect(() => {
    const scrollArea = document.querySelector(".scroll-area")
    if (scrollArea) {
      scrollArea.scrollTop = scrollArea.scrollHeight
    }
  }, [messages]) // Removed unnecessary dependencies: activeSession

  const handleSessionSelect = (id: string) => {
    setActiveSession(id)
    setIsLoadingMessages(true)
    setMessages([])
    // Simulate fetching messages for the selected session
    setTimeout(() => {
      setMessages(mockMessages[id] || [])
      setIsLoadingMessages(false)
    }, 1000)
    setIsSidebarOpen(false)
  }

  const handleNewSession = () => {
    const newSession: ChatSession = {
      id: Date.now().toString(),
      name: "New Chat",
    }
    setSessions([newSession, ...sessions])
    handleSessionSelect(newSession.id)
  }

  const handleSendMessage = () => {
    if (input.trim() && activeSession) {
      const newMessage: Message = { role: "user", content: input.trim() }
      setMessages([...messages, newMessage])
      setInput("")
      // Simulate AI response
      setTimeout(() => {
        const aiResponse: Message = { role: "assistant", content: "This is a simulated AI response." }
        setMessages((prevMessages) => [...prevMessages, aiResponse])
      }, 1000)
    }
  }

  const handleLightModeSwitch = () => {
    setIsWarningModalOpen(true)
  }

  const handleConfirmLightMode = () => {
    setIsWarningModalOpen(false)
    setHasShownWarning(true)
    setTheme("light")
    console.log("Light mode switched", theme)
  }

  const handleCancelLightMode = () => {
    setIsWarningModalOpen(false)
  }

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen)
  }

  return (
    <div
      className={`flex h-screen bg-gradient-to-br from-yellow-light to-yellow dark:from-background dark:to-background ${playfair.variable}`}
    >
      {/* Sidebar */}
      <Sidebar
        sessions={sessions}
        activeSession={activeSession}
        onNewSession={handleNewSession}
        onSessionSelect={handleSessionSelect}
        isOpen={isSidebarOpen}
        onClose={() => setIsSidebarOpen(false)}
        isLoading={isLoadingSessions}
      />

      {/* Main Content */}
      <div className="flex flex-col flex-1 overflow-hidden">
        {/* Top bar */}
        <div className="bg-yellow dark:bg-turquoise p-4 flex items-center justify-between shadow-md">
          <div className="flex items-center">
            <Button variant="ghost" size="icon" onClick={toggleSidebar} className="mr-2 md:hidden">
              <Menu className="h-6 w-6 text-yellow-dark dark:text-turquoise-light" />
            </Button>
            <PlatypusIcon />
            <h1 className="text-xl md:text-2xl font-bold text-yellow-dark dark:text-turquoise-light font-playfair">
              Chatypus
            </h1>
          </div>
          <ThemeToggle onLightModeSwitch={handleLightModeSwitch} />
        </div>

        {/* Chat Area */}
        <div className="flex-1 flex flex-col px-4 md:px-8 lg:px-12 overflow-hidden py-0">
          <ScrollArea className="flex-1 pr-4 scroll-area">
            <div className="max-w-4xl lg:max-w-6xl mx-auto">
              <AnimatePresence>
                {isLoadingMessages
                  ? // Loading skeletons for messages
                    Array.from({ length: 5 }).map((_, index) => (
                      <motion.div
                        key={`skeleton-${index}`}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className={cn("mb-4", index % 2 === 0 ? "text-right" : "text-left")}
                      >
                        <Skeleton
                          className={cn("inline-block h-12 rounded-2xl", index % 2 === 0 ? "w-3/4 ml-auto" : "w-3/4")}
                        />
                      </motion.div>
                    ))
                  : messages.map((message, index) => (
                      <motion.div
                        key={index}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        className={cn("mb-4 flex", message.role === "user" ? "justify-end" : "justify-start")}
                      >
                        <div
                          className={cn(
                            "p-3 rounded-2xl max-w-[80%] break-words bg-transparent",
                            message.role === "user" ? "ml-auto" : "mr-auto"
                          )}
                        >
                          {message.content}
                        </div>
                      </motion.div>
                    ))}
              </AnimatePresence>
            </div>
          </ScrollArea>
          <Separator className="my-6 opacity-20" />
          <div className="relative max-w-5xl lg:max-w-7xl mx-auto w-full my-3">
            <Input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message..."
              className="w-full h-14 pr-12 pl-6 bg-background border-2 border-foreground/20 focus:border-foreground/50 transition-all duration-300 rounded-full text-lg"
              onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
              disabled={!activeSession || isLoadingMessages}
            />
            <button
              onClick={handleSendMessage}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-foreground/50 hover:text-foreground transition-colors duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
              disabled={!activeSession || isLoadingMessages}
            >
              <Send className="h-6 w-6" />
            </button>
          </div>
        </div>
      </div>
      <LightModeWarningModal
        isOpen={isWarningModalOpen}
        onConfirm={handleConfirmLightMode}
        onCancel={handleCancelLightMode}
      />
      <Overlay isOpen={isSidebarOpen} onClose={() => setIsSidebarOpen(false)} />
    </div>
  )
}

