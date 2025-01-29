import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog"

interface LightModeWarningModalProps {
  isOpen: boolean
  onConfirm: () => void
  onCancel: () => void
}

export function LightModeWarningModal({ isOpen, onConfirm, onCancel }: LightModeWarningModalProps) {
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return null
  }

  return (
    <Dialog open={isOpen} onOpenChange={onCancel}>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle className="text-xl md:text-2xl font-bold text-yellow-dark dark:text-turquoise">
            Warning
          </DialogTitle>
          <DialogDescription className="text-gray-700 dark:text-gray-300 text-sm md:text-base">
            There is a reason why this site is in dark mode by default. Are you sure you want to be blinded?
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className="sm:justify-start">
          <Button
            variant="outline"
            onClick={onCancel}
            className="w-full sm:w-auto border-yellow dark:border-turquoise text-yellow-dark dark:text-turquoise rounded-2xl"
          >
            No, keep it dark
          </Button>
          <Button
            onClick={onConfirm}
            className="w-full sm:w-auto bg-yellow dark:bg-turquoise text-yellow-dark dark:text-turquoise-light rounded-2xl"
          >
            Yes, I&apos;m sure
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}

